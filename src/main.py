from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api.swagger import router as swagger_router
from api.urls import router as api_router
from config import Config as settings


title = 'Авторы и книги'
description = 'API работы с авторами и книгами'

app = FastAPI(debug=settings.DEBUG, title=title, docs_url=None, redoc_url=None)
app.openapi_version = '3.0.0'
app.include_router(api_router, prefix='/api', tags=['api'])

app.include_router(swagger_router)

app.mount('/static', StaticFiles(directory='{path}/static'.format(path=settings.BASE_DIR)), name='static')
