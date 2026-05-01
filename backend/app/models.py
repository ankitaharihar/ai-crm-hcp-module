from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    product = Column(String)
    interest = Column(String)
    summary = Column(Text)