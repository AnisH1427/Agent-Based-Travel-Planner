from workflows.main_workflow import workflow
from agents.research_agent import research_agent
from agents.budget_agent import budget_agent
from agents.logistic_agent import logistics_agent
from supervisor.supervisor import supervisor
from langgraph.graph import END
from tools.file_writer import file_writer

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
    user_input = input("What kind of trip would you like to plan?\nYour answer: ")
    result = app.invoke({"user_input": user_input, "current_step": "research"})

    print("\n==== Travel Planner Results ====")
    print("\n[Research Results]\n", result.get("research_data", "No research data found."))
    print("\n[Budget Estimate]\n", result.get("budget_data", "No budget data found."))
    print("\n[Final Plan]\n", result.get("final_plan", "No final plan generated."))
    print("\n===============================\n")

    # Save results to file
    file_writer.write_plan(f"User Input: {user_input}\n\nResearch Results:\n{result.get('research_data', '')}\n\nBudget Estimate:\n{result.get('budget_data', '')}\n\nFinal Plan:\n{result.get('final_plan', '')}")
    print("Results have been saved to travel_plan.md.")
