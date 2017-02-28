import React from 'react';
import { preview } from '../misc_utils'

export default function CuisineList({ cuisines, setSelected, selected }) {
  const cuisineItems = cuisines.map(cuisine => {
    const className = cuisine === selected ? "selected" : "";
    const clickHandler = () => setSelected(cuisine);
    return (
      <li key={ cuisine } onClick={ clickHandler } className={ className }>
        <a href="javascript:void(0)">{ preview(cuisine, 16) }</a>
      </li>
    );
  });
  return (
    <section className="cuisine-list full">
      <h3>Cuisines</h3>
      <ul>
        { cuisineItems }
      </ul>
    </section>
  );
}
