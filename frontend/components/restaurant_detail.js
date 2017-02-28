import React from 'react';
import { formatAddress, capitalize } from '../misc_utils'

const whitelist = [
  "cuisine_description",
  "max_grade",
  "total_score",
  "phone"
];

const colNames = {
  camis: "Camis",
  cuisine_description: "Cuisine",
  max_grade: "Grade",
  total_score: "Score",
  phone: "Phone Number",
  inspection_date: "Inspection Date"
};

export default function RestaurantDetail({ restaurant, rank }) {
  if (!restaurant) return null;
  const cols = whitelist.map((col, idx) => {
    return (
      <li key={ idx }>
        <strong>{ capitalize(colNames[col]) }: </strong>
        { restaurant[col] }
      </li>
    )
  });

  return (
    <article className="flex-item restaurant-detail">
      <h3>#{ rank } <i>-</i> { capitalize(restaurant.dba) }</h3>
      <ul>
        <li>
          <strong>Address: </strong>
          { formatAddress(restaurant) }
        </li>
        { cols }
      </ul>
    </article>
  );
}
