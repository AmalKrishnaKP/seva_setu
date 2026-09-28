from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, UUID, String, Float, Boolean, DateTime, Index,Integer,ARRAY,ForeignKey,DateTime,Enum
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from src.core.session import Base
from datetime import datetime,timezone
from core.enum import JobStatusEnum


class Job(Base):
    __tablename__="jobs"
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    category_id=Column(
        UUID,
        ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False
    )
    geo_location = Column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=True
    ) 
    discription=Column(
        String(225),
        nullable=False
    )
    audio=Column(
        String(225),
        nullable=True
    )
    created_at=Column(
        DateTime,
        default=datetime.now(timezone.utc)

    )
    customer_id=Column(
        UUID(as_uuid=True),
        ForeignKey("user.id",ondelete="CASCADE")
    )
    worker_id=Column(
        UUID(as_uuid=True),
        ForeignKey("worker.id",ondelete="CASCADE")
    )
    status=role = Column(
        Enum(JobStatusEnum),
        nullable=False
    )
    customer= relationship(
            "Customer",
            back_populates="user",
            cascade="all, delete-orphan",
    
        )
    worker= relationship(
            "Worker",
            back_populates="worker",
            cascade="all, delete-orphan",
    
        )