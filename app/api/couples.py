from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from app.crud import couple as couple_crud
from app.schemas.couple import CoupleCreate, CoupleUpdate, CoupleInDB
from app.database.session import get_db

router = APIRouter(tags=["couples"])


# Роут для получения всех пар
@router.get("/couples", response_model=list[CoupleInDB])
async def get_couples(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    couples = await couple_crud.get_couples(db, skip=skip, limit=limit)
    return couples


# Роут для получения пары по ID
@router.get("/couples/{couple_id}", response_model=CoupleInDB)
async def get_couple(couple_id: int, db: AsyncSession = Depends(get_db)):
    couple = await couple_crud.get_couple(db, couple_id)
    if not couple:
        raise HTTPException(status_code=404, detail="Couple not found")
    return couple


# Роут для получения пар для группы в определенный диапазон дат
@router.get("/couples/group/{group_id}", response_model=list[CoupleInDB])
async def get_couples_by_group_and_date(
    group_id: int,
    start_date: date,
    end_date: date,
    db: AsyncSession = Depends(get_db),
):
    couples = await couple_crud.get_couples_by_group_and_date(
        db, group_id, start_date, end_date
    )
    return couples


# Роут для создания новой пары
@router.post("/couples", response_model=CoupleInDB)
async def create_couple(
    couple: CoupleCreate, db: AsyncSession = Depends(get_db)
):
    db_couple = await couple_crud.create_couple(db, couple)
    return db_couple


# Роут для обновления пары
@router.put("/couples/{couple_id}", response_model=CoupleInDB)
async def update_couple(
    couple_id: int, couple: CoupleUpdate, db: AsyncSession = Depends(get_db)
):
    db_couple = await couple_crud.update_couple(db, couple_id, couple)
    if not db_couple:
        raise HTTPException(status_code=404, detail="Couple not found")
    return db_couple


# Роут для удаления пары
@router.delete("/couples/{couple_id}", response_model=CoupleInDB)
async def delete_couple(couple_id: int, db: AsyncSession = Depends(get_db)):
    db_couple = await couple_crud.delete_couple(db, couple_id)
    if not db_couple:
        raise HTTPException(status_code=404, detail="Couple not found")
    return db_couple
