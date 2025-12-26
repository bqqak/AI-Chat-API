# 🤖 AI Chat API

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

A lightweight, full-stack AI chat application that acts as a proxy to **Google's Gemini API**. It features automatic chat history tracking based on client IP addresses, eliminating the need for complex user registration for quick demos.

Built with **FastAPI** for high performance and **SQLAlchemy** for robust data persistence.

## ✨ Features

* **⚡ High-Performance Backend:** Powered by FastAPI and Uvicorn.
* **🧠 Google Gemini Integration:** Seamlessly forwards user prompts to Google's generative AI models.
* **💾 Smart Persistence:** Automatically saves prompt/response history using **SQLite**.
* **📍 IP-Based Session Tracking:** Retrieves chat history for users based on their IP address (no login required).
* **🌐 CORS Enabled:** Ready for frontend integration (React, Vue, or vanilla JS).
* **📃 Auto-Documentation:** Interactive API docs via Swagger UI (`/docs`).

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **Server:** Uvicorn
* **Database:** SQLite, SQLAlchemy (ORM)
* **AI Model:** Google Gemini API (`google-generativeai`)
* **Frontend:** Simple HTML/JS (or connect your own React app)

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or higher
* A Google Gemini API Key (Get it [here](https://aistudio.google.com/app/apikey))

### Usage
Start the Backend Server

Run the Uvicorn server with hot-reload enabled:
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

Access the Frontend

If you have the index.html file in the root, you can open it directly in your browser or serve it using a live server (e.g., VS Code Live Server) on port 5500.
