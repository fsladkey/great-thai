import React, { Component } from 'react';
import Chart from 'chart.js'
import { formatAddress, capitalize } from '../misc_utils'

const NYC_LAT_LNG = {
  lat: 40.7128, lng: -74.0059
}

export default class GradeDistibutionChart extends Component {
  constructor(props) {
    super(props);
    this.markers = []
  }

  componentDidMount() {
    this.map = new google.maps.Map(this.mapNode, {
      zoom: 10,
      center: NYC_LAT_LNG
    });
    this.setMarkers(this.props.restaurants);
  }

  placeMarker = (resaurant, idx) => {
    const geocoder = new google.maps.Geocoder();
    const address =  { address: formatAddress(resaurant) };
    geocoder.geocode(address, (results, status) => {
      if (status == google.maps.GeocoderStatus.OK) {
        const infowindow = new google.maps.InfoWindow({
          content: resaurant.dba
        });

        const marker = new google.maps.Marker({
          map: this.map,
          title: resaurant.dba,
          animation: google.maps.Animation.DROP,
          position: results[0].geometry.location
        });
        marker.addListener('click', () => {
          infowindow.open(this.map, marker);
          this.props.setSelected(idx)
        });

        this.markers.push(marker);
      }
    });
  }

  clearMarker = (marker) => {
    marker.setMap(null);
  }

  setMarkers(restaurants) {
    this.markers.forEach(this.clearMarker);
    this.markers = [];
    restaurants.forEach(this.placeMarker);
  }

  getRef = mapNode => {
    if (!mapNode) return;
    this.mapNode = mapNode;
  }

  render() {
    return (
      <div className="container flex-item">
        <div id="map" ref={ this.getRef }/>
      </div>
    )
  }
}
