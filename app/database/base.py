from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models import Student, Teacher, Couple, Discipline, Day, Group
