from pydantic import BaseModel
from datetime import date


class CoupleBase(BaseModel):
    discipline_id: int
    teacher_id: int
    group_id: int
    date: date
    number_pair: int
    cabinet: str | None = None


class CoupleCreate(CoupleBase):
    pass


class CoupleUpdate(CoupleBase):
    pass


class CoupleInDB(CoupleBase):
    id: int

    class Config:
        orm_mode = True
