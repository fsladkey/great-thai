import React from 'react';
import RetaurantIndexItem from './restaurant_index_item';

export default function TopRestaurants({ restaurants, setSelected, selectedIdx }) {
  const restaurantItems = restaurants.map((restaurant, idx) =>
    <RetaurantIndexItem
      setSelected={ () => setSelected(idx) }
      selected={ selectedIdx === idx }
      restaurant={ restaurant }
      key={ restaurant.id }
      rank={ idx + 1 }
      />
  );
  return (
    <ol className="restaurant-list flex-row">
      { restaurantItems }
    </ol>
  );
}
