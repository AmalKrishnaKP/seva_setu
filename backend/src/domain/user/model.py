import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, String, Float, Boolean, DateTime, Index,Integer
from geoalchemy2 import Geography
from core.session import base

class User(base):
    __tablename__="user"
    id=Column(UUID,primary_key=True,default=uuid.uuid4)
    name=Column(String(100),nullable=False)
    phone=Column(String(100),nullable=False)
    email=Column(String(225))
    password_hash=Column(String(225),nullable=False)
    is_verified=Column(Boolean,nullable=False,default=False)

    latitude=Column(Float,nullable=False)
    longitude=Column(Float,nullable=False)
    geo_location = Column(Geography(geometry_type="POINT",srid=4326),nullable=True)

    address=Column(String(225),nullable=False)

    profile_img=Column(String(225))

    verification_proof=Column(String(225))

    exp_yrs=Column(Float)
    salary=Column(Float)
    service_radius=Column(Integer)
    average_rating=Column(Float)
    total_rating=Column(Integer)
    status=Column(Boolean)

    created_at = Column(DateTime,nullable=False,
                        default=lambda: datetime.now(timezone.utc))

    updated_at = Column(DateTime,nullable=False,
                        default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc)
    )
    __table_args__ = (
        Index(
            "idx_users_geo_location",
            "geo_location",
            postgresql_using="gist"
        ),
    )
    