from pydantic import BaseModel

class Student(BaseModel):
    name: str

student = Student(name="Alice")
print(type(student))
