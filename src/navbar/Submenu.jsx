import { useState } from "react";
import { Link } from "react-router";

function Submenu({ title, items, isOpen, onToggle }) {
  return (
    <li key={title}>
        {title}
      <ul className={`d-bg-base-100 d-rounded-t-none d-p-2 ${isOpen ? "" : "hidden"}`}>
        {items.map((item) => (
          <li key={item.id}>
            <Link to={item.path}>{item.label}</Link>
          </li>
        ))}
      </ul>
    </li>
  );
}

export default Submenu;
