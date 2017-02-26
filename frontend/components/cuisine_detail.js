import React, { Component } from 'react';
import { fetchCuisineStats } from '../api_util'
import Loader from './loader'
import TopRestaurants from './top_restaurants'
import GradeDistributionChart from './grade_distribution_chart'

export default class CuisineDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stats: {},
      fetching: true
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

  setSelected = (selected) => {
    this.setState({ selected });
  }

  render() {
    const { fetching, stats } = this.state;
    if (fetching) return <Loader />;

    return (
      <section>
        <TopRestaurants restaurants={ stats.top_ten }/>
        <GradeDistributionChart
          data={ stats.grade_distribution }
          cuisine={ this.props.cuisine }
          />
      </section>
    );
  }
}
