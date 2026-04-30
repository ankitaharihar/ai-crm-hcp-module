from fastapi import FastAPI

from .schemas import InteractionCreate
from .services.ai_parser import parse_interaction_text

app = FastAPI(title="AI-First CRM API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/interactions/parse")
def parse_interaction(payload: InteractionCreate) -> dict:
    structured_data = parse_interaction_text(payload.notes)
    return {"input": payload.model_dump(), "parsed": structured_data}