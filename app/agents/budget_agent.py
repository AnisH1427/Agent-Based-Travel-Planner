from config.llm_config import llm

def budget_agent(state):
    print("[BudgetAgent] Received state:", state)
    research_data = state.get("research_data", "")
    prompt = f"""
    You are a budget analyst.
    Estimate costs based on: {research_data}
    Include flights, accommodation, food, activities.
    Use calculator tool if needed.
    """
    response = llm.invoke(prompt)
    new_state = {**state, "budget_data": response.content}
    # print("[BudgetAgent] Returning state:", new_state)
    return new_state
