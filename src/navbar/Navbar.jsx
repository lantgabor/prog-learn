import { HashRouter, Routes, Route, Link } from "react-router";
import { useState } from "react";

import Submenu from "./Submenu";

function Navbar() {
  const [openMenu, setOpenMenu] = useState(null);

  const toggleMenu = (menu) => {
    setOpenMenu(openMenu === menu ? null : menu);
  };

  return (
    <nav className="d-navbar d-bg-base-100 d-shadow-sm">
      <Link className="d-btn d-btn-ghost d-text-xl" to="/">Home</Link>
      <ul className="d-menu d-menu-horizontal d-px-1">
        <Submenu
          title="Course"
          items={[{ label: "Introduction", path: "/course/intro" }]}
          isOpen={openMenu === "course"}
          onToggle={() => toggleMenu("course")}
        />
        <Submenu
          title="Extras"
          items={[
            { label: "Hello", path: "/extras/hello" },
            { label: "GFM", path: "/extras/gfm" },
            { label: "Math", path: "/extras/mmath" },
          ]}
          isOpen={openMenu === "extras"}
          onToggle={() => toggleMenu("extras")}
        />
      </ul>
    </nav>
  );
}

export default Navbar;
