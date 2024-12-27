from pydantic import BaseModel
from typing import Optional


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupBase):
    pass


class GroupInDBBase(GroupBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Group(GroupInDBBase):
    pass
