import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_MODEL = "mistralai/mistral-7b-instruct:free"
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    
    # RAG Config
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Web Search Config
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # Add this line