import os
from pathlib import Path

from dotenv import load_dotenv


dotenv_path = '.env'
load_dotenv(dotenv_path)


class Config:
    """Настройки."""

    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'app')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', '5432'))
    DB_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

    DEBUG = os.environ.get('DEBUG', False)
    RELOAD = os.environ.get('DEBUG', False)

    APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
    APP_PORT = int(os.environ.get('APP_PORT', '8000'))
    APP_WORKERS = int(os.environ.get('APP_WORKERS', '2'))

    BASE_DIR = Path(__file__).resolve().parent
    MIGRATION_FILE = f'{BASE_DIR}/migrations/init_migration.txt'
