import React from 'react';
import { formatAddress, capitalize } from '../misc_utils'

const whitelist = [
  "cuisine_description",
  "grade",
  "score",
  "phone"
];

const col_names = {
  cuisine_description: "Cuisine",
  grade: "Grade",
  score: "Score",
  phone: "Phone Number"
};

export default function RestaurantDetail({ restaurant, rank }) {
  if (!restaurant) return null;
  const cols = whitelist.map(col => {
    return (
      <li key={ col_names[col] }>
        <strong>{ capitalize(col) }: </strong>
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
