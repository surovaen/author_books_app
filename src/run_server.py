import uvicorn

from config import Config as settings


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.RELOAD,
        workers=settings.APP_WORKERS,
    )
