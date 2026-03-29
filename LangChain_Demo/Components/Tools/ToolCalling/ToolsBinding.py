from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_openai import ChatOpenAI

load_dotenv()

# Tool creation

@tool()
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b, return their product."""
    return a * b
print(multiply.invoke({'a':3, 'b':4}))  # Output: 12
print(multiply.description)  # Output: "Given 2 numbers a and b, return their product."
print(multiply.args_schema)  # Output: {'a': <class 'int'>, 'b': <class 'int'>}
print(multiply.name)  # Output: "multiply"
print(multiply.args) # Output: {'a': 3, 'b': 4}
      
# Tool binding
llm = ChatOpenAI(model="gpt-3.5-mini")
llm_with_tools =llm.bind_tools([multiply])
