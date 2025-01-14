from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Discipline
from app.schemas.discipline import DisciplineCreate, DisciplineUpdate


async def get_disciplines(db: AsyncSession, skip: int = 0, limit: int = 100):
    async with db.begin():
        result = await db.execute(select(Discipline).offset(skip).limit(limit))
        return result.scalars().all()


async def get_discipline(db: AsyncSession, discipline_id: int):
    async with db.begin():
        result = await db.execute(
            select(Discipline).filter(Discipline.id == discipline_id)
        )
        return result.scalar_one_or_none()


async def create_discipline(db: AsyncSession, discipline: DisciplineCreate):
    db_discipline = Discipline(name=discipline.name)
    db.add(db_discipline)
    await db.commit()
    return db_discipline


async def update_discipline(
    db: AsyncSession, discipline_id: int, discipline: DisciplineUpdate
):
    db_discipline = await get_discipline(db, discipline_id)
    if db_discipline:
        db_discipline.name = discipline.name
        await db.commit()
        return db_discipline
    return None


async def delete_discipline(db: AsyncSession, discipline_id: int):
    db_discipline = await get_discipline(db, discipline_id)
    if db_discipline:
        await db.delete(db_discipline)
        await db.commit()
        return db_discipline
    return None
