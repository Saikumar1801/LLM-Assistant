# test_llm.py
from agents import get_llm

llm = get_llm()
response = llm.invoke("Hello, how are you?")
print(response)