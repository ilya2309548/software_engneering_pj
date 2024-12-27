from sqlalchemy import Column, Integer, ForeignKey, String, Date
from app.database.base import Base


class Couple(Base):
    __tablename__ = "couples"

    id = Column(Integer, primary_key=True, index=True)
    discipline_id = Column(Integer, ForeignKey("disciplines.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    date = Column(Date, nullable=False)
    number_pair = Column(Integer, nullable=False)
    cabinet = Column(String, nullable=True)
