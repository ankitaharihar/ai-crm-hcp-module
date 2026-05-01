from pydantic import BaseModel


class InputText(BaseModel):
    text: str


class InteractionCreate(BaseModel):
    doctor_name: str
    product: str
    interest: str
    summary: str