from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplayInput(BaseModel):
    a: int = Field(description='The first number to add')
    b: int = Field(description='The second number to add')

class MultiplayTool(BaseTool):
    name: str = 'multiply'
    description : str = 'multiply two numbers'
    args_schema : Type[BaseModel] = MultiplayInput

    def _run(self, a:int, b:int)-> float:
        return a * b

multiply_tool = MultiplayTool()
result = multiply_tool.invoke({'a':5, 'b': 10})
print(result)