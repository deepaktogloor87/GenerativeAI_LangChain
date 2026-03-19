from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'John Doe'
    age : Optional[int] = None
    email : EmailStr

new_student = {'age':35, 'email':'deepaktogloor@gmail.com'}
student = Student(**new_student)
print(student)
