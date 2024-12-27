from sqlalchemy import Column, Integer, Date
from app.database.base import Base


class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)


# class Day(Base):
#     __tablename__ = "days"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     date = Column(Date, nullable=False)
#     day_of_week = Column(String, nullable=False)

#     def __init__(self, date, name):
#         self.date = date
#         self.name = name
#         self.day_of_week = self.calculate_day_of_week()

#     @staticmethod
#     def calculate_day_of_week(date):
#         return date.strftime("%A")  # На английском
