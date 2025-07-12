from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize the Tavily client
# Make sure the API key starts with 'tvly-'
tavily = TavilyClient(api_key=TAVILY_API_KEY)

def search_tool(query: str) -> str:
    """
    A wrapper around Tavily Search.
    Uses the official Tavily SDK to perform a web search.
    """
    try:
        results = tavily.search(query)
        print("[DEBUG] Tavily raw response:", results)  # Debug print
        if not results or "results" not in results or not results["results"]:
            return "No data found from Tavily. Check your API key and query."
        context = "\n".join([f"{r['title']}: {r['content']}" for r in results["results"]])
        return context
    except Exception as e:
        return f"Error during search: {str(e)}"

