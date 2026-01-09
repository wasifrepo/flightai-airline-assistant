# ✈️ FlightAI – Multimodal Airline AI Assistant

FlightAI is a **production-style, multimodal AI customer support assistant** for an airline.  
It combines **LLM-powered conversation**, **tool calling with a real database**, and **image + audio generation** in a single interactive web application.

This project demonstrates how modern AI systems can be built using **agentic workflows**, clean Python architecture, and real integrations rather than hard-coded responses.

---

## 🚀 Features

- 💬 Conversational AI assistant for airline customer support
- 🧠 Tool calling / agentic behavior (LLM decides when to query tools)
- 🗄️ SQLite database integration for ticket price lookups
- 🖼️ Image generation for destination previews
- 🔊 Text-to-speech audio responses
- 🧩 Modular, production-style Python architecture
- 🌐 Interactive Gradio web UI
- 🔐 Secure environment variable handling (no secrets in code)

---

## 🧠 How It Works (High Level)

1. User sends a message via the Gradio UI
2. The LLM analyzes the request
3. If required, the LLM **calls a tool** (e.g. ticket price lookup)
4. The backend executes the tool (SQLite query)
5. The LLM generates a final response using the tool result

Optional:
- Generate an image for the destination
- Generate spoken audio for the response

This mirrors how real **agentic AI systems** are designed in production.

---

## 🏗️ Architecture Overview

User
↓
Gradio UI
↓
LLM (OpenAI Chat API)
↓
Tool Calls (when needed)
├── SQLite DB (ticket prices)
├── Image Generation
└── Text-to-Speech
↓
Final Multimodal Response (Text + Image + Audio)

## 🛠️ Tech Stack

- Python 3.12
- OpenAI API (Chat, Tools, Image Generation, TTS)
- Gradio (Web UI)
- SQLite (Local database)
- uv (Modern Python package & environment manager)
- Pillow (Image handling)

---

## 📂 Project Structure

flightai_airline_assistant/
├── app/
│ ├── main.py # Application entry point
│ ├── config.py # Configuration & constants
│ ├── prompts.py # System prompts
│ ├── services/ # Business logic (DB, image, audio, OpenAI)
│ ├── tools/ # Tool schemas & handlers
│ └── ui/ # Gradio UI
│
├── database/
│ ├── seed_prices.sql # DB schema & seed data
│ └── build_db.py # DB creation script
│
├── docs/ # Documentation & screenshots
├── .env.example # Environment variable template
├── pyproject.toml # Dependencies (uv)
├── uv.lock # Locked dependency versions
└── README.md

---


## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/flightai_airline_assistant.git
cd flightai_airline_assistant

### 2️⃣ Create environment variables

Create a .env file at the project root:
OPENAI_API_KEY=your_openai_api_key_here

.env is ignored by git and never committed.

### 3️⃣ Install dependencies (using uv)
uv sync

### 4️⃣ Build the database
uv run python database/build_db.py

### 5️⃣ Run the application
uv run python -m app


The app will open automatically at:
http://127.0.0.1:7860

---

🧪 Example Interactions

User:
Hi, how are you?

Assistant:
Hello! I'm doing well, thank you. How can I assist you with your flight today?

User:
I'd like to enquire about the ticket price for a flight to Paris?

Assistant:
The price for a return ticket to Paris is $450.

(With generated image + audio response)

![Chat Interface Example](docs/UIexample.png)

---

🔐 Security & Best Practices

API keys stored in .env (never committed)
Database generated locally (not pushed to GitHub)
Modular codebase with clear separation of concerns
No hard-coded secrets or credentials