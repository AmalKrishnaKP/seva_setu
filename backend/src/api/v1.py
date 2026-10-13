from fastapi import APIRouter
from domain.auth.router import router as auth_router
from domain.user.router import  router as user_rotuer
router=APIRouter(prefix="/v1")

router.include_router(user_rotuer)
router.include_router(auth_router)