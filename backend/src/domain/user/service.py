from core.responce import error_response,success_response
from domain.user.repository import userRepo
def get_employee_10km(db,lati,long):
    try:
        repo=userRepo(db)
        data=repo.user_in_10km(lati,long)
        return success_response(status_code=200,message="retrived",data=data)
    except Exception as e:
        print(e)
        return error_response(status_code=401,message="server side error")