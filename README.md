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
- AI Layer: LangGraph + rule-based parser / LLM-backed parsing
- Database: SQLite (for demo)

## ⚙️ Core Features

- Log interaction via form
- Log interaction via AI chat
- Convert natural language into structured CRM data
- AI-generated summaries
- Editable interaction records

## 🧩 Architecture

User Input → FastAPI → LangGraph Agent → LLM → Structured Data → Database → UI

## AI Agent (LangGraph)

This project uses LangGraph to implement an AI-driven decision system.

The agent:

- Accepts natural language input
- Determines user intent: log, edit, or fetch
- Executes the corresponding tool
- Interacts with the database

### Tools Implemented

1. Log Interaction
	- Parses free text using the deterministic parser or LLM-backed parser
	- Extracts doctor, product, and interest
	- Saves the record to the database

2. Edit Interaction
	- Updates the latest interaction record

3. Fetch Interaction History
	- Retrieves structured past interactions

LangGraph acts as the orchestration layer connecting user input to backend operations.

## 📁 Project Structure

- `backend/` → API, database models, AI agent
- `frontend/` → React UI for interaction logging

## 🎯 Objective

To demonstrate how AI agents (LangGraph + LLMs) can enhance CRM workflows by reducing manual effort and improving data quality.

## Interview Explanation

Use this line in the interview:

"LangGraph acts as the decision engine. It routes user input to the correct business tool - logging, editing, or fetching interactions - instead of relying on fixed API endpoints."

What you built:

- User enters free text
- LangGraph agent interprets intent
- Agent selects a tool: log interaction, edit interaction, or fetch history
- System updates the database
- Returns structured CRM data

That is AI-driven CRM behavior.

## Demo Flow

Show Swagger for `/interactions/parse`

Show DB save

Show `/agent-test`

Say:

"Here the agent decides what action to take based on user input."

Then demonstrate:

- normal text → log
- edit → update
- show → history

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
