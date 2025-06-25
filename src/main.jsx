import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import Hello from "./Hello.mdx";
import Gfm from "./Gfm.mdx";
import MMath from "./MMath.mdx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
    <Hello />
    <Gfm />
    <MMath />
  </StrictMode>,
);
