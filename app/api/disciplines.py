from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import discipline as discipline_crud
from app.schemas.discipline import (
    DisciplineCreate,
    DisciplineUpdate,
    DisciplineInDB,
)
from app.database.session import get_db

router = APIRouter(prefix="/disciplines", tags=["disciplines"])


# Роут для получения всех дисциплин
@router.get("/disciplines", response_model=list[DisciplineInDB])
async def get_disciplines(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    disciplines = await discipline_crud.get_disciplines(
        db, skip=skip, limit=limit
    )
    return disciplines


# Роут для получения дисциплины по ID
@router.get("/disciplines/{discipline_id}", response_model=DisciplineInDB)
async def get_discipline(
    discipline_id: int, db: AsyncSession = Depends(get_db)
):
    discipline = await discipline_crud.get_discipline(db, discipline_id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return discipline


# Роут для создания новой дисциплины
@router.post("/disciplines", response_model=DisciplineInDB)
async def create_discipline(
    discipline: DisciplineCreate, db: AsyncSession = Depends(get_db)
):
    db_discipline = await discipline_crud.create_discipline(db, discipline)
    return db_discipline


# Роут для обновления дисциплины
@router.put("/disciplines/{discipline_id}", response_model=DisciplineInDB)
async def update_discipline(
    discipline_id: int,
    discipline: DisciplineUpdate,
    db: AsyncSession = Depends(get_db),
):
    db_discipline = await discipline_crud.update_discipline(
        db, discipline_id, discipline
    )
    if not db_discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline


# Роут для удаления дисциплины
@router.delete("/disciplines/{discipline_id}", response_model=DisciplineInDB)
async def delete_discipline(
    discipline_id: int, db: AsyncSession = Depends(get_db)
):
    db_discipline = await discipline_crud.delete_discipline(db, discipline_id)
    if not db_discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline
