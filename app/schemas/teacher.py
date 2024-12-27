from pydantic import BaseModel
from typing import Optional


# Базовая схема для всех Teacher
class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    email: str
    discipline_id: int


# Схема для создания Teacher
class TeacherCreate(TeacherBase):
    pass


# Схема для обновления Teacher
class TeacherUpdate(TeacherBase):
    pass


# Схема для представления Teacher
class TeacherInDB(TeacherBase):
    id: int

    class Config:
        orm_mode = True
