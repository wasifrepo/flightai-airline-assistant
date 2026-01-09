✈️ FlightAI – Multimodal Airline AI Assistant

FlightAI is a production-style, multimodal AI customer support assistant for an airline.
It combines LLM-powered conversation, tool calling with a real database, and image + audio generation in a single interactive web application.

This project demonstrates how modern AI systems can be built using agentic workflows, clean Python architecture, and real integrations rather than hard-coded responses.

🚀 Features

💬 Conversational AI assistant for airline customer support

🧠 Tool calling / agentic behavior (LLM decides when to query tools)

🗄️ SQLite database integration for ticket price lookups

🖼️ Image generation for destination previews

🔊 Text-to-speech audio responses

🧩 Modular, production-style Python architecture

🌐 Interactive Gradio web UI

🔐 Secure environment variable handling (no secrets in code)

🧠 How It Works (High Level)

User sends a message via the Gradio UI

The LLM analyzes the request

If required, the LLM calls a tool (e.g. ticket price lookup)

The backend executes the tool (SQLite query)

The LLM generates a final response using the tool result

Optional:

Generate an image for the destination

Generate spoken audio for the response

This mirrors how real agentic AI systems are designed in production.

🏗️ Architecture Overview
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

🛠️ Tech Stack

Python 3.12

OpenAI API (Chat, Tools, Image Generation, TTS)

Gradio (Web UI)

SQLite (Local database)

uv (Modern Python package & environment manager)

Pillow (Image handling)

📂 Project Structure
flightai_airline_assistant/
├── app/
│   ├── main.py               # Application entry point
│   ├── config.py             # Configuration & constants
│   ├── prompts.py            # System prompts
│   ├── services/             # Business logic (DB, image, audio, OpenAI)
│   ├── tools/                # Tool schemas & handlers
│   └── ui/                   # Gradio UI
│
├── database/
│   ├── seed_prices.sql       # DB schema & seed data
│   └── build_db.py           # DB creation script
│
├── docs/                     # Documentation & screenshots
├── .env.example              # Environment variable template
├── pyproject.toml            # Dependencies (uv)
├── uv.lock                   # Locked dependency versions
└── README.md

⚙️ Setup & Run Locally
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/flightai_airline_assistant.git
cd flightai_airline_assistant

2️⃣ Create environment variables

Create a .env file at the project root:

OPENAI_API_KEY=your_openai_api_key_here


.env is ignored by git and never committed.

3️⃣ Install dependencies (using uv)
uv sync

4️⃣ Build the database
uv run python database/build_db.py

5️⃣ Run the application
uv run python -m app


The app will open automatically in your browser at:

http://127.0.0.1:7860

🧪 Example Interactions

User:

How much is a ticket to London?

Assistant:

A return ticket to London costs $520.

User:

Tell me about Paris.

Assistant:

Paris is a popular destination known for its culture, landmarks, and cuisine.

(With generated image + audio response)

🔐 Security & Best Practices

API keys are stored in .env (never committed)

Database file is generated locally (not pushed to GitHub)

Modular codebase with clear separation of concerns

No hard-coded secrets or credentials

📈 Future Improvements

✈️ Flight booking workflow (mock or real)

🪑 Seat selection and baggage pricing tools

👤 User sessions & memory

📊 Logging and observability

☁️ Cloud deployment (Railway, Fly.io, Hugging Face Spaces)

🧪 Automated tests

👨‍💻 Why This Project Matters

This project is designed to showcase:

Real LLM tool-calling patterns

Clean, maintainable Python architecture

Practical multimodal AI usage

Production-oriented thinking rather than demos or notebooks

It reflects how AI assistants are built in real engineering teams.