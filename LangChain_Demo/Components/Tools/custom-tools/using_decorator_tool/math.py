from langchain_community.tools import tool

   
@tool
def addition(a:int, b:int) -> int:
    '''Add the two numbers'''
    return a + b

@tool
def substraction(a:int, b:int) -> int:
    '''substract the two numbers'''
    return a - b

@tool
def multiplication(a:int, b:int) -> float:
    '''multiplies the two numbers'''
    return a * b

@tool
def division(a:int, b:int) -> float:
    '''divides the two numbers and return the result in floating'''
    return a / b

@tool
def division_floor(a:int, b:int) -> int:
    '''divides the two numbers and return the result in floor division in integer'''
    return a // b
    

result = multiplication.invoke({'a':3,'b':5})
print(multiplication.name)
print(multiplication.description)
print(multiplication.args)
print(multiplication.args_schema.model_json_schema())