import asyncio

from database import run_migration


if __name__ == '__main__':
    asyncio.run(run_migration())
