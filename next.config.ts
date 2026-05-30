import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Pin the workspace root to this project. A stray package-lock.json in the
  // user's home directory was otherwise being inferred as the root.
  turbopack: {
    root: import.meta.dirname,
  },
};

export default nextConfig;
