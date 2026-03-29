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
def BoundedTool():
    """A tool that is bound to a specific LLM."""
    llm = ChatOpenAI(model="gpt-4o-mini")
    return llm.bind_tools([multiply])

# Tool calling
llm_with_tools = BoundedTool()
response = llm_with_tools.invoke("can you multiply 5 and 6?")
print(response.tool_calls[0])  # Output: "The product of 5 and 6 is 30."