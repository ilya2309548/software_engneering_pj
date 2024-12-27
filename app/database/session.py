from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .base import Base
import os
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Создаем движок для асинхронной работы
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем фабрику для сессий
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


# Инициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        # Выполняем создание таблиц
        await conn.run_sync(Base.metadata.create_all)


# Получение сессии для работы с БД
async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
