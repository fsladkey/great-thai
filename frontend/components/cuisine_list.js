import React from 'react';

function preview(string, maxLen) {
  return string.length > maxLen ? string.slice(0, maxLen) + "..." : string;
}

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
    <ul className="cuisine-list">
      { cuisineItems }
    </ul>
  );
}
