from fastapi import APIRouter


router=APIRouter(prefix="/auth")


@router.post(("send otp"))
def otp_send(
    
)