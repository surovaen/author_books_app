import aiofiles
from sqlalchemy import MetaData, text
from sqlalchemy.ext.asyncio import create_async_engine

from config import Config as settings


engine = create_async_engine(settings.DB_URL)
metadata = MetaData()


async def run_migration():
    """Запуск миграций."""
    async with aiofiles.open(settings.MIGRATION_FILE, 'r') as file:
        migration = await file.readlines()

    async with engine.connect() as conn:
        async with conn.begin():
            for operation in migration:
                await conn.execute(text(operation.strip('\n')))
