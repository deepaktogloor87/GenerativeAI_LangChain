from pydantic import BaseModel

class Student(BaseModel):
    name: str = 'John Doe'

student = Student()
print(student.name)
