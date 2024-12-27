from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Discipline(Base):
    __tablename__ = "disciplines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
