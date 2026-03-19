from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'John Doe'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(..., gt=0.0, lt=10.0, description="CGPA must be between 0.0 and 10.0")


new_student = {'age':35, 'email':'deepaktogloor@gmail.com', 'cgpa': 8.5 }
student = Student(**new_student)
print(student.model_dump_json)
