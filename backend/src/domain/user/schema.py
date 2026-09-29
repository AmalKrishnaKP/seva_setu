from pydantic import BaseModel
from src.core.enum import LanguageEnum

class Create_User(BaseModel):
    name:str
    language:LanguageEnum
    