from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html


router = APIRouter()


@router.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    """Переопределение сваггера."""
    return get_swagger_ui_html(
        openapi_url='/openapi.json',
        title='Api Document',
        swagger_js_url='/static/swagger-ui-bundle.js',
        swagger_css_url='/static/swagger-ui.css',
    )
