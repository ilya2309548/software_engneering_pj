from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Couple
from app.schemas.couple import CoupleCreate, CoupleUpdate
from datetime import date


# Функция для получения всех пар
async def get_couples(db: AsyncSession, skip: int = 0, limit: int = 100):
    async with db.begin():
        result = await db.execute(select(Couple).offset(skip).limit(limit))
        return result.scalars().all()


# Функция для получения пары по ID
async def get_couple(db: AsyncSession, couple_id: int):
    async with db.begin():
        result = await db.execute(select(Couple).filter(Couple.id == couple_id))
        return result.scalar_one_or_none()


# Функция для получения пар для группы в определенный диапазон дат
async def get_couples_by_group_and_date(
    db: AsyncSession, group_id: int, start_date: date, end_date: date
):
    async with db.begin():
        result = await db.execute(
            select(Couple)
            .filter(Couple.group_id == group_id)
            .filter(Couple.date >= start_date)
            .filter(Couple.date <= end_date)
            .order_by(Couple.date, Couple.number_pair)
        )
        return result.scalars().all()


# Функция для создания новой пары
async def create_couple(db: AsyncSession, couple: CoupleCreate):
    db_couple = Couple(**couple.dict())
    db.add(db_couple)
    await db.commit()
    return db_couple


# Функция для обновления пары
async def update_couple(db: AsyncSession, couple_id: int, couple: CoupleUpdate):
    db_couple = await get_couple(db, couple_id)
    if db_couple:
        db_couple.discipline_id = couple.discipline_id
        db_couple.teacher_id = couple.teacher_id
        db_couple.group_id = couple.group_id
        db_couple.date = couple.date
        db_couple.number_pair = couple.number_pair
        db_couple.cabinet = couple.cabinet
        await db.commit()
        return db_couple
    return None


# Функция для удаления пары
async def delete_couple(db: AsyncSession, couple_id: int):
    db_couple = await get_couple(db, couple_id)
    if db_couple:
        await db.delete(db_couple)
        await db.commit()
        return db_couple
    return None
