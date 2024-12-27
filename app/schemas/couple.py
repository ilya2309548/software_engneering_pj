from pydantic import BaseModel
from datetime import date


# Базовая схема для пары
class CoupleBase(BaseModel):
    discipline_id: int
    teacher_id: int
    group_id: int
    date: date
    number_pair: int
    cabinet: str | None = None


# Схема для создания новой пары
class CoupleCreate(CoupleBase):
    pass


# Схема для обновления пары
class CoupleUpdate(CoupleBase):
    pass


# Схема для представления пары
class CoupleInDB(CoupleBase):
    id: int

    class Config:
        orm_mode = True
