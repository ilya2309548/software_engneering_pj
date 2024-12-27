from pydantic import BaseModel


class DisciplineBase(BaseModel):
    name: str


class DisciplineCreate(DisciplineBase):
    pass


class DisciplineUpdate(DisciplineBase):
    pass


class DisciplineInDB(DisciplineBase):
    id: int

    class Config:
        orm_mode = True
