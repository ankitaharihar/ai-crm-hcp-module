from pydantic import BaseModel, Field


class InteractionCreate(BaseModel):
    hcp_name: str = Field(min_length=1)
    notes: str = Field(min_length=1)
    interaction_type: str = Field(default="general")