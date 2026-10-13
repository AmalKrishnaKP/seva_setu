from pydantic import BaseModel
from core.enum import LanguageEnum

class Create_User(BaseModel):
    name:str
    language:LanguageEnum
    phone:int
    latitude:float
    longitude:float
    
class location(BaseModel):
    lati:float
    longi:float