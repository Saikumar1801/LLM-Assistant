from langchain_core.prompts import ChatPromptTemplate
from agents import get_llm

class ResponseAgent:
    def __init__(self):
        self.llm = get_llm()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a professional AI assistant. Format responses with:
            - Clear section headings
            - Bullet points for key concepts
            - Accurate technical details
            - Proper markdown formatting"""),
            ("human", "{input}")
        ])
        self.chain = self.prompt | self.llm
    
    def respond(self, research_result: str, user_query: str) -> str:
        return self.chain.invoke({
            "input": f"Research Context:\n{research_result}\n\nUser Query: {user_query}\n\nProvide a professional, detailed response:"
        })