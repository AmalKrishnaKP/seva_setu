from core.session import base
from sqlalchemy import Column,UUID,String,Float,Boolean,Integer,Date
import uuid

class User(base):
    __tablename__="user"
    id=Column(UUID,primary_key=True,default=uuid.uuid4)
    name=Column(String(100),nullable=False)
    phone=Column(String(100),nullable=False)
    email=Column(String(225))
    password_hash=Column(String(225),nullable=False)
    profile_img=Column(String(225))
    address=Column(String(225))
    latitude=Column(Float,nullable=False)
    longitude=Column(Float,nullable=False)
    verification_proof=Column(String(225))
    is_verified=Column(Boolean,nullable=False)
    exp_yrs=Column(Float)
    salary=Column(Float,nullable=False)
    service_radius=Column(Integer,nullable=False)
    average_rating=Column(Float)
    total_rating=Column(Integer)
    status=Column(Boolean,nullable=False)
    created_at=Column(Date,nullable=False)
    updated_at=Column(Date,nullable=False)
    # geo_location=Column(ur_datatype)