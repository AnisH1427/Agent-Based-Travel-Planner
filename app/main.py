from workflows.main_workflow import workflow
from agents.research_agent import research_agent
from agents.budget_agent import budget_agent
from agents.logistic_agent import logistics_agent
from supervisor.supervisor import supervisor
from langgraph.graph import END
from tools.TravelScript import plan_scribe

# Import LLM and tools to ensure they are initialized
from config.llm_config import llm
from tools.web_search import search_tool

# Add nodes to the workflow
workflow.add_node("research", research_agent)
workflow.add_node("budget", budget_agent)
workflow.add_node("logistics", logistics_agent)
workflow.add_node("supervisor", supervisor)
workflow.add_node("complete", lambda state: state)  # Dummy node for completion

# Set entry point
workflow.set_entry_point("research")

# Conditional edges
workflow.add_conditional_edges(
    "supervisor",
    lambda x: x["current_step"],
    {
        "research": "research",
        "budget": "budget",
        "logistics": "logistics",
        "complete": END,
    }
)

workflow.add_edge("research", "supervisor")
workflow.add_edge("budget", "supervisor")
workflow.add_edge("logistics", "supervisor")

app = workflow.compile()

if __name__ == "__main__":
    while True:
        user_input = input("What kind of trip would you like to plan? \nAlso include Origin and Destinatin: \nYour answer: ")
        # Use LLM to check if the query is travel-related before invoking the workflow
        check_prompt = (
            f"Is the following request about planning a trip or travel? Return only 'true' or 'false'.\nRequest: {user_input}"
        )
        check_response = llm.invoke(check_prompt)
        if hasattr(check_response, 'content'):
            is_travel = check_response.content.strip().lower()
        else:
            is_travel = str(check_response).strip().lower()
        if is_travel == 'true':
            break
        print("Sorry, I can only answer travel-related queries. Please describe your trip or travel plans.")

    state = {"user_input": user_input, "current_step": "research"}

    # Human-in-the-loop for research
    state = research_agent(state)
    print("\n[Research Results]\n", state.get("research_data", "No research data."))
    feedback = input("Do you want to proceed with this research result? (yes/no/revise): ").strip().lower()
    if feedback == "revise":
        state["user_input"] = input("Please provide revised trip details: ")
        state = research_agent(state)
        print("\n[Research Results]\n", state.get("research_data", "No research data."))
    elif feedback != "yes":
        print("Exiting workflow.")
        exit()

    state["current_step"] = "budget"
    # Human-in-the-loop for budget
    state = budget_agent(state)
    print("\n[Budget Estimate]\n", state.get("budget_data", "No budget data."))
    feedback = input("Do you want to proceed with this budget estimate? (yes/no/revise): ").strip().lower()
    if feedback == "revise":
        state["user_input"] = input("Please provide revised trip details for budget: ")
        state = budget_agent(state)
        print("\n[Budget Estimate]\n", state.get("budget_data", "No budget data."))
    elif feedback != "yes":
        print("Exiting workflow.")
        exit()

    state["current_step"] = "logistics"
    # Human-in-the-loop for logistics
    state = logistics_agent(state)
    print("\n[Final Plan]\n", state.get("final_plan", "No final plan generated."))
    feedback = input("Do you want to proceed with this final plan? (yes/no/revise): ").strip().lower()
    if feedback == "revise":
        state["user_input"] = input("Please provide revised trip details for itinerary: ")
        state = logistics_agent(state)
        print("\n[Final Plan]\n", state.get("final_plan", "No final plan generated."))
    elif feedback != "yes":
        print("Exiting workflow.")
        exit()

    # Save results to file
    plan_scribe.write_plan(f"User Input: {state['user_input']}\n\nResearch Results:\n{state.get('research_data', '')}\n\nBudget Estimate:\n{state.get('budget_data', '')}\n\nFinal Plan:\n{state.get('final_plan', '')}")
    print("Results have been saved to travel_plan.md.")
