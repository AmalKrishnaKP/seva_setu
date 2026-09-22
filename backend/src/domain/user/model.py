from datetime import datetime, timezone
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, String, Float, Boolean, DateTime, Index,Integer
from geoalchemy2 import Geography
from core.session import base

from sqlalchemy import Column, UUID, String, Float, Boolean, DateTime, Index
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from src.core.session import Base


class User(Base):
    __tablename__ = "users"

    # Identity
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # Common details
    name = Column(
        String(100),
        nullable=False
    )

    phone = Column(
        String(15),
        nullable=False,
        unique=True
    )

    email = Column(
        String(255),
        unique=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    profile_img = Column(
        String(500)
    )

    # Location
    address = Column(
        String(500),
        nullable=False
    )

    latitude = Column(
        Float,
        nullable=False
    )

    longitude = Column(
        Float,
        nullable=False
    )

    # PostGIS
    geo_location = Column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=True
    )

    # Account
    status = Column(
        Boolean,
        nullable=False,
        default=True
    )

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    sessions = relationship(
        "UserSession",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    worker = relationship(
        "Worker",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index(
            "idx_users_geo_location",
            "geo_location",
            postgresql_using="gist"
        ),
    )
