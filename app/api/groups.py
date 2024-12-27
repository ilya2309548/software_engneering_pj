from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.group import Group, GroupCreate, GroupUpdate
from app.crud.group import (
    get_group,
    get_groups,
    create_group,
    update_group,
    delete_group,
)
from app.database.session import get_db

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=List[Group])
async def read_groups(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    return await get_groups(db, skip=skip, limit=limit)


@router.get("/{group_id}", response_model=Group)
async def read_group(group_id: int, db: AsyncSession = Depends(get_db)):
    db_group = await get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@router.post("/", response_model=Group)
async def create_new_group(
    group: GroupCreate, db: AsyncSession = Depends(get_db)
):
    return await create_group(db, group=group)


@router.put("/{group_id}", response_model=Group)
async def update_existing_group(
    group_id: int, group: GroupUpdate, db: AsyncSession = Depends(get_db)
):
    db_group = await update_group(db, group_id=group_id, group=group)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@router.delete("/{group_id}", response_model=Group)
async def delete_existing_group(
    group_id: int, db: AsyncSession = Depends(get_db)
):
    db_group = await delete_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group
