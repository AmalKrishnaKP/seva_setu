from domain.user import services
from core import session
# from sys import prefix
from fastapi import APIRouter

from domain.user.schema import location
router=APIRouter(prefix="/user")

@router.post("/location")
def location_address(
    loc:location
):
    return services.location_address(loc.lati,loc.longi)