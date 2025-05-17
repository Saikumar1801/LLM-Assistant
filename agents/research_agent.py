from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from agents import get_llm
from tools.web_search import get_web_search_tool
from tools.doc_retriever import DocRetriever

class ResearchAgent:
    def __init__(self):
        self.llm = get_llm()
        
        # Initialize tools
        self.tools = []
        
        # Add web search if configured
        web_search = get_web_search_tool()
        if "not configured" not in web_search.description:
            self.tools.append(web_search)
        
        # Add document retriever
        self.tools.append(DocRetriever().retrieve_documents)
        
        # Correct prompt template with proper message types
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a research assistant. Answer questions using available tools.
            
            Available Tools:
            {tools}
            
            Use this format:
            
            Question: input question
            Thought: think about what to do
            Action: action to take ({tool_names})
            Action Input: input to action
            Observation: result of action
            ... (repeat as needed)
            Thought: I know the final answer
            Final Answer: final response"""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3
        )
    
    def research(self, query: str) -> str:
        try:
            result = self.executor.invoke({
                "input": query,
                "agent_scratchpad": []  # Must be empty list, not None
            })
            return result["output"]
        except Exception as e:
            print(f"Research error: {str(e)}")
            return "I couldn't complete the research. Please try again."