from .openrouter_llm import OpenRouterLLM
from config import Config

def get_llm():
    return OpenRouterLLM(
        temperature=0.7,
        max_tokens=1000
    )