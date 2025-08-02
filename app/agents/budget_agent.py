from config.llm_config import llm

def budget_agent(state):
    print("[BudgetAgent] Received state:", state)
    research_data = state.get("research_data", "")
    prompt = f"""
    You are a budget analyst.
    Estimate the costs for the trip based on: {research_data}
    Return the result as a clear key-value list, where each key is an expense category (e.g., flights, accommodation, food, activities, transportation, miscellaneous) and each value is the estimated cost in INR. Do not include extra explanations or scenarios.
    Example format:
    flights: 12000
    accommodation: 7000
    food: 3500
    activities: 2000
    transportation: 1500
    miscellaneous: 1000
    """
    response = llm.invoke(prompt)
    new_state = {**state, "budget_data": response.content}
    print("Budget agent executed successfully.")
    return new_state
