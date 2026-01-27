# 🤖 React Chatbot Frontend

## Project Overview

This project is the **frontend** for an intelligent NLP chatbot built with **React.js**.  
It interacts with a Python backend that handles:

- Predefined knowledge-based Q&A
- TF-IDF similarity matching
- Wikipedia API fallback for unknown questions

Users can send messages via a **chat interface** and get responses from the bot in real-time.

---

## Technologies Used

- **React.js** – UI library
- **JavaScript (ES6)** – Frontend logic
- **CSS** – Styling
- **jQuery** – Simplified API calls (for AJAX)
- **Python Backend** – FastAPI / Flask (serving chatbot logic)

---

## 📂 Project Structure

frontend/
│
├── src/
│ │ └── ChatBot.js # Chat interface
│ ├── App.js # Main React app
│ ├── index.js # App entry point
│ └── ChatBot.css # Chat styling
├── package.json # Frontend dependencies
└── README.md # Documentation

---

## Installation & Setup

### Step 1️: Clone the repository

```bash
git clone <your-repo-url>
cd frontend
```

## Step 2️: Install dependencies

npm install

## Step 3️: Run the React app

npm start

## The app runs on http://localhost:3000
