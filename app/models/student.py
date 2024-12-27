from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=True, index=True)
    middle_name = Column(String, nullable=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))
