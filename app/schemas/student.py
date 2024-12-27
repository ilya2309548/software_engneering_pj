from pydantic import BaseModel
from typing import Optional


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    email: str
    group_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentInDBBase(StudentBase):
    id: int

    class Config:
        orm_mode = True


class Student(StudentInDBBase):
    pass
