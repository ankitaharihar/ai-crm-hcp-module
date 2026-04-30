# AI-First CRM (HCP Interaction Module)

This project is a mini AI-powered CRM system focused on logging interactions with Healthcare Professionals (HCPs). It demonstrates an AI-first approach where users can log interactions using either a structured form or natural language via chat.

## 🚀 Key Idea

Instead of manually filling forms, users can simply type:

"Met Dr Sharma, discussed insulin, he is interested, follow up next week"

The system uses an LLM to:

- Extract structured data
- Generate summaries
- Suggest next actions

## 🧠 Tech Stack

- Frontend: React + Redux
- Backend: FastAPI (Python)
- AI Layer: LangGraph + Groq (gemma2-9b-it)
- Database: SQLite (for demo)

## ⚙️ Core Features

- Log interaction via form
- Log interaction via AI chat
- Convert natural language into structured CRM data
- AI-generated summaries
- Editable interaction records

## 🧩 Architecture

User Input → FastAPI → LangGraph Agent → LLM → Structured Data → Database → UI

## 📁 Project Structure

- `backend/` → API, database models, AI agent
- `frontend/` → React UI for interaction logging

## 🎯 Objective

To demonstrate how AI agents (LangGraph + LLMs) can enhance CRM workflows by reducing manual effort and improving data quality.

## 🛠️ Setup (coming next)

Instructions to run the project will be added after implementation.

## 🔥 Why this matters

👉 Recruiter kya dekhega:

“AI-first thinking hai ya nahi?”
“Concept samjha hai ya sirf code kiya hai?”

👉 Ye README clearly dikha raha:

understanding ✔️
clarity ✔️
intent ✔️

## 🧠 Next step

Abhi sab set hai.

👉 bol “backend ready”
ab hum:

proper AI JSON parsing fix
LangGraph integration (real wala)
clean API flow

banayenge 🔥
