# agents/base.py

from agents.openrouter_llm import OpenRouterLLM

def get_llm(temperature: float = 0.7, max_tokens: int = 1000):
    """
    Returns an instance of the OpenRouter LLM with given parameters.
    
    Args:
        temperature: Controls randomness in output.
        max_tokens: Maximum tokens in the response.
    
    Returns:
        Configured LLM instance.
    """
    return OpenRouterLLM(temperature=temperature, max_tokens=max_tokens)
