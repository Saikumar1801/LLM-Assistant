from agents.research_agent import ResearchAgent
from agents.response_agent import ResponseAgent
from tools.doc_retriever import DocRetriever
from langchain_core.messages import AIMessage, HumanMessage

def load_sample_data():
    return """
    Large Language Models (LLMs) like Mistral-7B are transformer-based neural networks.
    They are trained on vast text datasets to understand and generate human-like text.
    RAG (Retrieval-Augmented Generation) combines LLMs with external knowledge retrieval.
    Multi-agent systems use specialized agents working together to solve complex tasks.
    """

def main():
    # Initialize components
    research_agent = ResearchAgent()
    response_agent = ResponseAgent()
    doc_retriever = DocRetriever()
    
    # Load knowledge base
    doc_retriever.load_documents(load_sample_data())
    
    print("Welcome to the LLM Assistant!")
    while True:
        query = input("\nEnter your question (or 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            break
            
        if not query:
            print("Please enter a valid question.")
            continue
            
        try:
            # Research phase
            print("\nResearching...")
            research_result = research_agent.research(query)
            
            # Response phase
            print("\nGenerating response...")
            response = response_agent.respond(research_result, query)
            
            print("\nAssistant Response:")
            print(response)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or ask a different question.")

if __name__ == "__main__":
    main()