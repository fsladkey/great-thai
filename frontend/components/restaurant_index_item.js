import React from 'react';
import RetaurantIndexItem from './restaurant_index_item';

const DISPLAY_COLS = [
  "phone",
  "boro",
  "grade",
  "score"
]

function capitalize_single(word) {
  if (word.length === 0) return ""
  return word[0].toUpperCase() + word.slice(1).toLowerCase();
}

function capitalize(words) {
  return words.split(' ').map(capitalize_single).join(' ')
}

export default function RestaurantIndexItem({ restaurant, rank }) {
  const cols = DISPLAY_COLS.map(col =>
    <li key={ col }>
      <strong>{ capitalize(col) }: </strong>
      { restaurant[col] }
    </li>
  );
  return (
    <li>
      <h3>{ rank } - { capitalize(restaurant.dba) }</h3>
      <ul>
        { cols }
      </ul>
    </li>
  );
}
