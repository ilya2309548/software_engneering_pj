from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


async def get_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    return result.scalars().first()


async def get_students(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Student).offset(skip).limit(limit))
    return result.scalars().all()


async def create_student(db: AsyncSession, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student


async def update_student(
    db: AsyncSession, student_id: int, student: StudentUpdate
):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    db_student = result.scalars().first()
    if not db_student:
        return None
    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)
    await db.commit()
    await db.refresh(db_student)
    return db_student


async def delete_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    db_student = result.scalars().first()
    if db_student:
        await db.delete(db_student)
        await db.commit()
    return db_student
