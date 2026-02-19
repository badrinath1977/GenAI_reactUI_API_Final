# 🚀 Enterprise Copilot -- Department-Based AI Chrome Extension

Enterprise AI-powered Chrome Extension integrating **React
(TypeScript) + Vite + FastAPI backend**.

------------------------------------------------------------------------

## 🏗 Architecture Overview

React (Extension UI) ↓ API Client Layer ↓ FastAPI Backend ↓ Vector DB /
LLM Engine

------------------------------------------------------------------------

## 🛠 Tech Stack

### Frontend

-   React (TypeScript)
-   Vite
-   Chrome Extension (Manifest V3)
-   React-Markdown
-   Modular CSS

### Backend

-   FastAPI
-   REST APIs
-   CORS Middleware

------------------------------------------------------------------------

# 🛠 Setup & Build Guide

## 🚀 First Time Setup

Install all dependencies:

npm install

------------------------------------------------------------------------

## 🧹 Clean Build Setup

Delete existing dist folder before building.

### Windows (PowerShell)

Remove-Item -Recurse -Force dist

### Mac / Linux

rm -rf dist

------------------------------------------------------------------------

## 🔨 Build Extension (Production Mode)

npm run build

or

npx vite build

This generates the `dist/` folder for Chrome Extension.

------------------------------------------------------------------------

## 🖥 Run UI in Development Mode

npm run dev

Used for UI testing only (not extension mode).

------------------------------------------------------------------------

# 🔁 Automatic Clean Build Setup (Recommended)

## 1️⃣ Install Dev Dependency

npm install -D rimraf

## 2️⃣ Add Scripts in package.json

"scripts": { "dev": "vite", "build": "vite build", "clean": "rimraf
dist", "rebuild": "npm run clean && npm run build" }

## 3️⃣ Use Rebuild Command

npm run rebuild

------------------------------------------------------------------------

# 🧩 Chrome TypeScript Support

npm install --save-dev @types/chrome

------------------------------------------------------------------------

# 📦 Full Clean Reset (If Needed)

rm -rf node_modules dist package-lock.json npm install npm run build

------------------------------------------------------------------------

# 🌐 Load Extension in Chrome

1.  Open Chrome
2.  Go to chrome://extensions
3.  Enable Developer Mode
4.  Click Load Unpacked
5.  Select the dist/ folder

------------------------------------------------------------------------

# 🧠 Development Workflow

  Task                   Command
  ---------------------- -----------------
  Install dependencies   npm install
  Run UI locally         npm run dev
  Clean dist             npm run clean
  Build extension        npm run build
  Clean + Build          npm run rebuild

------------------------------------------------------------------------


# 🏁 Summary

Enterprise Copilot is a scalable, modular, department-aware AI extension
architecture designed for secure enterprise document interaction and
AI-driven summarization.
