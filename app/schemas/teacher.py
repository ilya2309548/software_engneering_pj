from pydantic import BaseModel
from typing import Optional


class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    email: str
    discipline_id: int


class TeacherCreate(TeacherBase):
    pass


class TeacherUpdate(TeacherBase):
    pass


class TeacherInDB(TeacherBase):
    id: int

    class Config:
        orm_mode = True
