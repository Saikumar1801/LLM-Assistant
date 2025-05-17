from langchain_community.tools.tavily_search import TavilySearchResults
from config import Config
from langchain_core.tools import Tool

def get_web_search_tool():
    if not hasattr(Config, 'TAVILY_API_KEY') or not Config.TAVILY_API_KEY:
        # Return a dummy tool if Tavily isn't configured
        return Tool(
            name="web_search",
            func=lambda x: "Web search is not configured",
            description="Searches the web (not configured)"
        )
    
    return TavilySearchResults(
        api_key=Config.TAVILY_API_KEY,
        max_results=3
    )