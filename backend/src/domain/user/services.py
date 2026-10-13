from core.addressLoca import addressLocator
from core.responce import success_response 
from core.transilator import transilator
def location_address(lati,longi):
    data=addressLocator(lati,longi)
    res=transilator(data=data,lang="tamil")


    return success_response(data=res,status_code=200,message="location retrived")


    
    
    # service for auto selecting address

    # select address from addresss where usrid==userid and gisditance btwn the location and address less than 10m