import { HashRouter, Routes, Route, Link } from "react-router";
import { useState } from "react";

import Submenu from "./Submenu";

function Navbar() {
  const [openMenu, setOpenMenu] = useState(null);

  const toggleMenu = (menu) => {
    setOpenMenu(openMenu === menu ? null : menu);
  };

  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
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
