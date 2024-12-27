from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.student import Student, StudentCreate, StudentUpdate
from app.crud.student import (
    get_student,
    get_students,
    create_student,
    update_student,
    delete_student,
)

from app.database.session import get_db

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=List[Student])
async def read_students(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    return await get_students(db, skip=skip, limit=limit)


@router.get("/{student_id}", response_model=Student)
async def read_student(student_id: int, db: AsyncSession = Depends(get_db)):
    db_student = await get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.post("/", response_model=Student)
async def create_new_student(
    student: StudentCreate, db: AsyncSession = Depends(get_db)
):
    return await create_student(db, student=student)


@router.put("/{student_id}", response_model=Student)
async def update_existing_student(
    student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_db)
):
    db_student = await update_student(
        db, student_id=student_id, student=student
    )
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.delete("/{student_id}", response_model=Student)
async def delete_existing_student(
    student_id: int, db: AsyncSession = Depends(get_db)
):
    db_student = await delete_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
