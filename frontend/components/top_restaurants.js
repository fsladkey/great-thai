import React from 'react';
import RetaurantIndexItem from './restaurant_index_item';

export default function TopRestaurants({ restaurants }) {
  const restaurantItems = restaurants.map((restaurant, idx) =>
    <RetaurantIndexItem
      restaurant={ restaurant }
      key={ restaurant.id }
      rank={ idx + 1 }
      />
  );
  return (
    <ol className="restaurant-list">
      { restaurantItems }
    </ol>
  );
}
