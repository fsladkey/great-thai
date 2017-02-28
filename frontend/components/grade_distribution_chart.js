import React, { Component } from 'react';
import Chart from 'chart.js'

function dataToMap(data) {
  const result = {}
  data.forEach(stat => {
    result[stat.grade] = stat.num_restaurants
  })
  return result
}

export default class GradeDistibutionChart extends Component {

  getChartData() {
    const data = dataToMap(this.props.data)
    const labels = Object.keys(data).sort()
    return {
      labels: labels,
      datasets: [
        {
          label: `Grade Distribution for ${this.props.cuisine}`,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1,
          data: labels.map(label => data[label]),
        }
      ]
    };
  }

  componentDidMount() {
    new Chart(this.chart, {
        type: 'horizontalBar',
        data: this.getChartData()
    });
  }

  getRef = chart => {
    if (!chart) return;
    this.chart = chart;
  }

  render() {
    return (
      <div className="container flex-item">
        <canvas ref={ this.getRef }/>
      </div>
    )
  }
}
