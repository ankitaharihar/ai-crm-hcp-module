from fastapi import FastAPI
from app.services.ai_parser import parse_interaction
from pydantic import BaseModel

from app.schemas import InteractionCreate 
from app.services.ai_parser import parse_interaction

app = FastAPI(title="AI-First CRM API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/interactions/parse")
def parse_interaction(payload: InteractionCreate) -> dict:
    structured_data = parse_interaction_text(payload.notes)
    return {"input": payload.model_dump(), "parsed": structured_data}
class InputText(BaseModel):
    text: str
@app.post("/interactions/parse")
def parse(data: InputText):
    return parse_interaction(data.text)