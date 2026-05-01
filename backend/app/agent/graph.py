from langgraph.graph import StateGraph
from typing import TypedDict

from app.database import SessionLocal
from app.models import Interaction
from app.services.ai_parser import parse_interaction_text


class AgentState(TypedDict):
    input: str
    output: dict


def agent_node(state: AgentState):
    text = state["input"].lower()
    db = SessionLocal()

    try:
        if "edit" not in text and "history" not in text and "show" not in text:
            parsed = parse_interaction_text(state["input"])
            interaction = Interaction(**parsed)
            db.add(interaction)
            db.commit()
            db.refresh(interaction)

            return {"output": {"action": "log", "data": parsed}}

        if "history" in text or "show" in text:
            data = db.query(Interaction).all()
            return {"output": {"action": "fetch", "data": [item.summary for item in data]}}

        if "edit" in text:
            return {"output": {"action": "edit", "message": "edit coming soon"}}

        return {"output": {"action": "unknown"}}
    finally:
        db.close()


graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
app_graph = graph.compile()