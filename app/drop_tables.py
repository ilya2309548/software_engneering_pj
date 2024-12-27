from app.database.session import engine
from app.database.base import Base
import asyncio


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    print("All tables dropped.")


# Запуск
if __name__ == "__main__":
    asyncio.run(drop_tables())
