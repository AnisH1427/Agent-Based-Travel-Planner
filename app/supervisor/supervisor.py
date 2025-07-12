def supervisor(state):
    print("\n Supervisor reviewing progress...")
    current_step = state.get("current_step", "research")

    if current_step == "research":
        return {"current_step": "budget"}
    elif current_step == "budget":
        return {"current_step": "logistics"}
    elif current_step == "logistics":
        return {"current_step": "complete"}
