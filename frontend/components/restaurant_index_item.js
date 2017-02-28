import React from 'react';
import RetaurantIndexItem from './restaurant_index_item';

export default function RestaurantIndexItem(props) {
  const { restaurant, rank, setSelected, selected } = props;
  const className = selected ? "selected" : "";
  return (
    <li onClick={ setSelected } className={ className }>
      <div className="restaurant-rank">
        { rank }
      </div>
      <div>
        { restaurant.dba }
      </div>
    </li>
  );
}
