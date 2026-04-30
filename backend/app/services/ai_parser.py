def parse_interaction_text(notes: str) -> dict:
    return {
        "summary": notes.strip(),
        "entities": [],
        "follow_up_required": False,
    }