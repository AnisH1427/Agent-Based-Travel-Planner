# agents/research_agent.py

from config.llm_config import llm
from tools.web_search import search_tool

def research_agent(state):
    print("[ResearchAgent] Received state:", state)
    user_input = state.get("user_input", "")

    # Improved prompt for higher quality search queries
    query_prompt = f"""
    You are a travel research expert. The user wants to plan a trip and provided this request:
    "{user_input}"
    Generate only one precise and optimized search query that is clear, focused, and suitable for a web search engine. Do not include any additional explanations or multiple options.
    """
    search_query = llm.invoke(query_prompt).content.strip()
    print(f"[ResearchAgent] Generated search query: {search_query}")

    # Use the search tool to get results
    search_result = search_tool(search_query)
    # print(f"[ResearchAgent] Search result: {search_result}")

    # Step 3: Return structured data
    new_state = {**state, "research_data": search_result}
    # print("[ResearchAgent] Returning state:", new_state)
    return new_state
