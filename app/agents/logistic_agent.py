from config.llm_config import llm

def logistics_agent(state):
    print("[LogisticsAgent] Received state:", state)
    research_data = state.get("research_data", "")
    budget_data = state.get("budget_data", "")
    prompt = f"""
    You are a logistics planner.
    Create a concise, medium-length, day-by-day itinerary for the user's trip using:
    Research: {research_data}
    Budget: {budget_data}
    Make sure to include:
    - Recommended destinations and attractions
    - Suggested activities for each day
    - Accommodation and transportation tips
    - Food and local experiences
    - Any travel tips or warnings
    Format the plan clearly and keep it easy to read. Avoid excessive details and keep the response medium in length.
    """
    response = llm.invoke(prompt)
    new_state = {**state, "final_plan": response.content}
    print("Logistics agent executed successfully.")
    return new_state
