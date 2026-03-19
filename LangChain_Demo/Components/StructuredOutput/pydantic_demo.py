from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = 'John Doe'
    age : Optional[int] = None

new_student = {'age':35}
student = Student(**new_student)
print(student)
