import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
// https://create-react-app.dev/docs/deployment/#notes-on-client-side-routing
import { HashRouter, Routes, Route, Link } from "react-router";
import "./index.css";
import "./CodeBlocks.css";
import "./fontsettings.css";
import "./App.css";

import Navbar from "./navbar/Navbar.jsx";
import App from "./App.jsx";
import Timer from "./timer/Timer.jsx";

// Dynamically import all page components
const modules = import.meta.glob("./pages/**/*.mdx", { eager: true });

const generateRoutes = () => {
  return Object.entries(modules).map(([path, module]) => {
    const Component = module.default;

    // Convert file path to route path
    const routePath =
      path
        .replace("./pages", "")
        .replace(/\.mdx$/, "")
        .replace(/\/index$/, "")
        .replace(/^\//, "") || "";

    return (
      <Route
        key={routePath || "/"}
        path={routePath.toLowerCase() || "/"}
        element={<Component />}
      />
    );
  });
};

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <HashRouter>
      <header>
        <Navbar />
        <Timer />
      </header>
      <main>
        <Routes>
          {generateRoutes()}
          <Route path="/" element={<App />} />
        </Routes>
      </main>
    </HashRouter>
  </StrictMode>
);
