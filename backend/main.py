from fastapi import FastAPI
from app.services.ai_parser import parse_interaction_text

from app.database import Base, SessionLocal, engine
from app.models import Interaction
from app.schemas import InputText, InteractionCreate

app = FastAPI(title="AI-First CRM API")
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/interactions/parse")
def parse(data: InputText):
    return parse_interaction_text(data.text)


@app.post("/interactions/save")
def save_interaction(data: InteractionCreate):
    db = SessionLocal()
    try:
        interaction = Interaction(**data.dict())
        db.add(interaction)
        db.commit()
        db.refresh(interaction)
        return interaction
    finally:
        db.close()


@app.put("/interactions/{id}")
def edit_interaction(id: int, data: InteractionCreate):
    db = SessionLocal()
    try:
        interaction = db.query(Interaction).filter(Interaction.id == id).first()

        if not interaction:
            return {"error": "Not found"}

        interaction.doctor_name = data.doctor_name
        interaction.product = data.product
        interaction.interest = data.interest
        interaction.summary = data.summary

        db.commit()
        db.refresh(interaction)
        return interaction
    finally:
        db.close()