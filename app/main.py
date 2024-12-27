from fastapi import FastAPI
from fastapi import FastAPI
from app.database.session import init_db
from app.api.groups import router as groups_router
from app.api.students import router as students_router
from app.api.teachers import router as teachers_router
from app.api.disciplines import router as disciplines_router
from app.api.couples import router as couples_router


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(students_router)
app.include_router(groups_router)
app.include_router(teachers_router)
app.include_router(disciplines_router)
app.include_router(couples_router)
