from fastapi import APIRouter
import domain.auth.service as service

router=APIRouter(prefix="/auth")


@router.post("/send_otp")
def otp_send(
    phone:int
):
    return service.otp_send(phone)

@router.post("/verify_otp")
def otp_verify(
    phone:int,
    otp:int
):
    return service.otp_verify(phone,otp)