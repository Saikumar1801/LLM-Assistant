# test_rag.py
from memory.vector_store import VectorStore

def test_rag():
    print("Testing RAG system...")
    
    # Initialize vector store
    vs = VectorStore()
    
    # Sample document
    doc = """Large Language Models (LLMs) are AI systems trained on vast amounts of text data.
    They can understand and generate human-like text. Examples include GPT-4 and Mistral-7B."""
    
    # Create vector store
    print("Creating vector store from document...")
    vs.create_from_documents(doc)
    
    # Test search
    print("\nSearching for 'What are LLMs?'...")
    results = vs.search("What are LLMs?")
    
    print("\nSearch Results:")
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(result.page_content)

if __name__ == "__main__":
    test_rag()