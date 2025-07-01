import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    extensions: [
      '.web.tsx', 
      '.web.ts', 
      '.web.jsx', 
      '.web.js', 
      '.tsx', 
      '.ts', 
      '.jsx', 
      '.js', 
      '.json'
    ],
    alias: {
      'components': path.resolve(__dirname, '../components/src'),
    },
  },
})
