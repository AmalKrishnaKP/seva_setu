from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from core.session import get_db
from domain.user import service
router=APIRouter(prefix="/user")


@router.get("/employee_in_10km_radius")
def get_employee_10km(
    lati:float,
    long:float,
    db:Session=Depends(get_db)
):
    return service.get_employee_10km(db,lati,long)