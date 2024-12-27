from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.group import Group
from app.schemas.group import GroupCreate, GroupUpdate


async def get_group(db: AsyncSession, group_id: int):
    result = await db.execute(select(Group).filter(Group.id == group_id))
    return result.scalars().first()


async def get_groups(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Group).offset(skip).limit(limit))
    return result.scalars().all()


async def create_group(db: AsyncSession, group: GroupCreate):
    db_group = Group(**group.dict())
    db.add(db_group)
    await db.commit()
    await db.refresh(db_group)
    return db_group


async def update_group(db: AsyncSession, group_id: int, group: GroupUpdate):
    result = await db.execute(select(Group).filter(Group.id == group_id))
    db_group = result.scalars().first()
    if not db_group:
        return None
    for key, value in group.dict(exclude_unset=True).items():
        setattr(db_group, key, value)
    await db.commit()
    await db.refresh(db_group)
    return db_group


async def delete_group(db: AsyncSession, group_id: int):
    result = await db.execute(select(Group).filter(Group.id == group_id))
    db_group = result.scalars().first()
    if db_group:
        await db.delete(db_group)
        await db.commit()
    return db_group
