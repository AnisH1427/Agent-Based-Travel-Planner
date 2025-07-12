from config.llm_config import llm

def logistics_agent(state):
    print("[LogisticsAgent] Received state:", state)
    research_data = state.get("research_data", "")
    budget_data = state.get("budget_data", "")
    prompt = f"""
    You are a logistics planner.
    Create a detailed, day-by-day itinerary for the user's trip using:
    Research: {research_data}
    Budget: {budget_data}
    Make sure to include:
    - Recommended destinations and attractions
    - Suggested activities for each day
    - Accommodation and transportation tips
    - Food and local experiences
    - Any travel tips or warnings
    Format the plan clearly and concisely for easy reading.
    """
    response = llm.invoke(prompt)
    new_state = {**state, "final_plan": response.content}
    return new_state
