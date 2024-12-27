from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate


async def get_teachers(db: AsyncSession, skip: int = 0, limit: int = 100):
    async with db.begin():
        result = await db.execute(select(Teacher).offset(skip).limit(limit))
        return result.scalars().all()


async def get_teacher(db: AsyncSession, teacher_id: int):
    async with db.begin():
        result = await db.execute(
            select(Teacher).filter(Teacher.id == teacher_id)
        )
        return result.scalar_one_or_none()


async def create_teacher(db: AsyncSession, teacher: TeacherCreate):
    db_teacher = Teacher(
        first_name=teacher.first_name,
        last_name=teacher.last_name,
        middle_name=teacher.middle_name,
        email=teacher.email,
        discipline_id=teacher.discipline_id,
    )
    db.add(db_teacher)
    await db.commit()
    return db_teacher


async def update_teacher(
    db: AsyncSession, teacher_id: int, teacher: TeacherUpdate
):
    db_teacher = await get_teacher(db, teacher_id)
    if db_teacher:
        db_teacher.first_name = teacher.first_name
        db_teacher.last_name = teacher.last_name
        db_teacher.middle_name = teacher.middle_name
        db_teacher.email = teacher.email
        db_teacher.discipline_id = teacher.discipline_id
        await db.commit()
        return db_teacher
    return None


async def delete_teacher(db: AsyncSession, teacher_id: int):
    db_teacher = await get_teacher(db, teacher_id)
    if db_teacher:
        await db.delete(db_teacher)
        await db.commit()
        return db_teacher
    return None
