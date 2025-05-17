from memory.vector_store import VectorStore
from langchain.tools import tool

class DocRetriever:
    def __init__(self):
        self.vs = VectorStore()
        self.loaded_docs = False
    
    @tool
    def retrieve_documents(self, query: str) -> str:
        """Retrieve relevant documents about LLMs and RAG systems"""
        if not self.loaded_docs:
            return "No documents loaded yet"
        docs = self.vs.search(query)
        return "\n\n".join([d.page_content for d in docs])
    
    def load_documents(self, text: str):
        self.vs.create_from_documents(text)
        self.loaded_docs = True