from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)

    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{9,14}$"
    )

    email: EmailStr | None = None

    address: str = Field(
        ...,
        min_length=3,
        max_length=500
    )

    latitude: float = Field(
        ...,
        ge=-90.0,
        le=90.0
    )

    longitude: float = Field(
        ...,
        ge=-180.0,
        le=180.0
    )
    
    profile_img: str | None = None


class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=128
    )

class UserUpdate(BaseModel):
    name: str | None = Field(
        None,
        min_length=2,
        max_length=100  
    )

    email: EmailStr | None = None
    address: str | None = Field(
        None,
        min_length=3,
        max_length=500
    )
    latitude: float | None = Field(
        None,
        ge=-90.0,
        le=90.0
    )
    longitude: float | None = Field(
        None,
        ge=-180.0,
        le=180.0
    )
    profile_img: str | None = None

class UserResponse(UserBase):
    id: UUID
    status: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
    

    
