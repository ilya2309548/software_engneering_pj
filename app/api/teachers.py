from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import teacher as teacher_crud
from app.schemas.teacher import TeacherCreate, TeacherUpdate, TeacherInDB
from app.database.session import get_db

router = APIRouter(prefix="/teachers", tags=["teachers"])


# Роут для получения всех учителей
@router.get("/teachers", response_model=list[TeacherInDB])
async def get_teachers(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    teachers = await teacher_crud.get_teachers(db, skip=skip, limit=limit)
    return teachers


# Роут для получения учителя по ID
@router.get("/teachers/{teacher_id}", response_model=TeacherInDB)
async def get_teacher(teacher_id: int, db: AsyncSession = Depends(get_db)):
    teacher = await teacher_crud.get_teacher(db, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


# Роут для создания нового учителя
@router.post("/teachers", response_model=TeacherInDB)
async def create_teacher(
    teacher: TeacherCreate, db: AsyncSession = Depends(get_db)
):
    db_teacher = await teacher_crud.create_teacher(db, teacher)
    return db_teacher


# Роут для обновления учителя
@router.put("/teachers/{teacher_id}", response_model=TeacherInDB)
async def update_teacher(
    teacher_id: int, teacher: TeacherUpdate, db: AsyncSession = Depends(get_db)
):
    db_teacher = await teacher_crud.update_teacher(db, teacher_id, teacher)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher


# Роут для удаления учителя
@router.delete("/teachers/{teacher_id}", response_model=TeacherInDB)
async def delete_teacher(teacher_id: int, db: AsyncSession = Depends(get_db)):
    db_teacher = await teacher_crud.delete_teacher(db, teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher
