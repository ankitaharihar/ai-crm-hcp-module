from langgraph.graph import StateGraph
from typing import TypedDict


class AgentState(TypedDict):
    input: str
    output: dict


def dummy_node(state: AgentState):
    return {
        "output": {
            "message": "LangGraph working"
        }
    }


graph = StateGraph(AgentState)
graph.add_node("start", dummy_node)
graph.set_entry_point("start")
app_graph = graph.compile()