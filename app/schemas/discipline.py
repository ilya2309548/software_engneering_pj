from pydantic import BaseModel


# Базовая схема для всех дисциплин
class DisciplineBase(BaseModel):
    name: str


# Схема для создания дисциплины
class DisciplineCreate(DisciplineBase):
    pass


# Схема для обновления дисциплины
class DisciplineUpdate(DisciplineBase):
    pass


# Схема для представления дисциплины
class DisciplineInDB(DisciplineBase):
    id: int

    class Config:
        orm_mode = True
