def log_interaction_tool(text: str):
    return {"action": "log", "text": text}


def edit_interaction_tool(id: int, data: dict):
    return {"action": "edit", "id": id, "data": data}


def get_history_tool(doctor_name: str):
    return {"action": "history", "doctor": doctor_name}


def followup_tool(text: str):
    return {"action": "followup", "suggestion": "Meet again in 2 days"}


def summary_tool(doctor_name: str):
    return {"action": "summary", "doctor": doctor_name}