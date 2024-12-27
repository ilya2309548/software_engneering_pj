from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    discipline_id = Column(Integer, ForeignKey("disciplines.id"))
