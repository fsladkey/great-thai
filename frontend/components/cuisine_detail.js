import React, { Component } from 'react';
import { fetchCuisineStats } from '../api_util'
import Loader from './loader'
import TopRestaurants from './top_restaurants'
import GradeDistributionChart from './grade_distribution_chart'
import RestaurantDetail from './restaurant_detail';
import RestaurantMap from './restaurant_map';

export default class CuisineDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stats: {},
      fetching: true,
      selectedIdx: 0
    };
  }

  componentDidMount() {
    fetchCuisineStats(this.props.cuisine).then(stats =>
      this.setState({ stats: stats, fetching: false })
    );
  }

  componentWillReceiveProps(nextProps) {
    this.setState({ fetching: true }, () => {
      fetchCuisineStats(nextProps.cuisine).then(stats =>
        this.setState({ stats: stats, fetching: false })
      );
    })
  }

  setSelected = (selectedIdx) => {
    this.setState({ selectedIdx });
  }

  selectedRestaurant() {
    return this.state.stats.top_ten[this.state.selectedIdx];
  }

  render() {
    const { fetching, stats } = this.state;
    if (fetching) return <Loader />;

    return (
      <section className="cuisine-detail full">
        <h1>{ this.props.cuisine }</h1>
        <TopRestaurants
          restaurants={ stats.top_ten }
          selectedIdx={ this.state.selectedIdx }
          setSelected={ this.setSelected }
          />
          <RestaurantDetail
            restaurant={ this.selectedRestaurant() }
            rank={ this.state.selectedIdx + 1 }
            />
          <section className="flex-row">
            <GradeDistributionChart
            data={ stats.grade_distribution }
            cuisine={ this.props.cuisine }
            />
            <RestaurantMap
              restaurants={ stats.top_ten }
              setSelected={ this.setSelected }
            />
        </section>
      </section>
    );
  }
}
