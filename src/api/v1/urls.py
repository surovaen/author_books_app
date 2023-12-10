from fastapi import APIRouter

from api.v1.routers import router as author_router


router = APIRouter()
router.include_router(author_router)
