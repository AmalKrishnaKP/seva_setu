import core.twilo as twilio
from core.responce import error_response,success_response
from core.token import create_access_token
def otp_send(phone):
    try:
        phoneStr="+91"+str(phone)
        res=twilio.otp_send(phone=phoneStr)
        if res=="pending":
            return success_response(status_code=201,message="otp created")
    except Exception as e:
        print(e)
        return error_response(status_code=500,message="error in otp service")
def otp_verify(phone,otp):
    try:
        PhoneStr=str(phone)
        PhoneStr="+91"+PhoneStr
        ans=twilio.verifi(phone=PhoneStr,otp=otp)
        if ans=="Approved":
            res=success_response(message="login successfully",data={"phone":phone})
            token=create_access_token(phone,role="null")
            
            res.set_cookie(
                key="access_token",
                value=token,
                max_age=60*60*24*7,
                secure=False,
                httponly=True,
                samesite="lax"
            )
        # print(res)

    except Exception as e:
        
        return error_response(status_code=500,message="error in otp service")
    if res=="pending":
        return error_response(status_code=401,message="incorrect otp") 
    elif res=="Approved":
        return success_response(status_code=200,message="correct otp")