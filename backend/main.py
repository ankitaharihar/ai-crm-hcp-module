from fastapi import FastAPI
from app.services.ai_parser import parse_interaction_text

from app.schemas import InputText

app = FastAPI(title="AI-First CRM API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/interactions/parse")
def parse(data: InputText):
    return parse_interaction_text(data.text)