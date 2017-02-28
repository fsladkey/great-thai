import React, { Component } from 'react';
import { fetchCuisines } from '../api_util'
import CuisineList from './cuisine_list'
import CuisineDetail from './cuisine_detail'
import Loader from './loader'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cuisines: [],
      selected: "Thai",
      fetching: true
    };
  }

  componentDidMount() {
    fetchCuisines().then(cuisines =>
      this.setState({ cuisines: cuisines.sort(), fetching: false })
    );
  }

  setSelected = (selected) => {
    this.setState({ selected });
  }

  render() {
    const { fetching, cuisines, selected } = this.state;
    if (fetching) return <Loader />;

    return (
      <main className="full flex-row">
        <CuisineList
          cuisines={ cuisines }
          setSelected={ this.setSelected }
          selected={ selected }
          />
        <CuisineDetail cuisine={ selected }/>
      </main>
    );
  }
}
