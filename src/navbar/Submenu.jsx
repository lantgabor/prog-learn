import { useState } from "react";
import { Link } from "react-router";

function Submenu({ title, items, isOpen, onToggle }) {
  return (
    <li onClick={onToggle}>
      <Link to={items[0].path}>{title}</Link>
      {isOpen && (
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              <Link to={item.path}>{item.label}</Link>
            </li>
          ))}
        </ul>
      )}
    </li>
  );
}

export default Submenu;
