def supervisor(state):
    print("\n Supervisor reviewing progress...")
    current_step = state.get("current_step", "research")

    # Stop execution if research agent found query is out of context
    if 'is_travel_related' in state and not state['is_travel_related']:
        print("Supervisor: Stopping workflow due to out-of-context query.")
        # Optionally, set a final_plan message for clarity
        return {**state, "current_step": "complete", "final_plan": "Sorry, I can only answer travel-related queries."}

    if current_step == "research":
        return {**state, "current_step": "budget"}
    elif current_step == "budget":
        return {**state, "current_step": "logistics"}
    elif current_step == "logistics":
        return {**state, "current_step": "complete"}
