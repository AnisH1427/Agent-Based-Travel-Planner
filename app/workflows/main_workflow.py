from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List

class AgentState(TypedDict):
    """State for the agent."""
    messages: Annotated[List[str], "List of messages exchanged with the agent."]
    user_input: str
    research_data: str
    budget_data: str
    final_plan: str
    current_step: str
    status: str

workflow = StateGraph(AgentState)

#Nodes will be added dynamically from agents and supervisor modules
