import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import mdx from "@mdx-js/rollup";
import tailwindcss from "@tailwindcss/vite";

import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";

import rehypeStarryNight from "rehype-starry-night";
import rehypeKatex from "rehype-katex";

import { ViteImageOptimizer } from 'vite-plugin-image-optimizer';

export default defineConfig({
  base: process.env.NODE_ENV === "production" ? "/prog-learn" : "/",
  plugins: [
    ViteImageOptimizer({
        /* pass your config */
      }),
    {
      enforce: "pre",
      ...mdx({
        remarkPlugins: [remarkGfm, remarkMath],
        rehypePlugins: [rehypeStarryNight, rehypeKatex],
        /* jsxImportSource: …, otherOptions… */
      }),
    },
    react(),
    tailwindcss(),
  ],
});
