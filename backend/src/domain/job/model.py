from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, UUID, String, Float, Boolean, DateTime, Index,Integer,ARRAY,ForeignKey,DateTime,Enum
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from core.session import Base
from datetime import datetime,timezone
from core.enum import JobStatusEnum


class Job(Base):
    __tablename__="jobs"
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    # category_id=Column(
    #     UUID,
    #     ForeignKey("categories.id", ondelete="CASCADE"),
    #     nullable=False
    # )
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
        ForeignKey("users.id",ondelete="CASCADE")
    )
    worker_id=Column(
        UUID(as_uuid=True),
        ForeignKey("workers.id",ondelete="CASCADE")
    )
    status= Column(
        Enum(JobStatusEnum),
        nullable=False
    )
    customer= relationship(
            "User"
        )
    worker= relationship(
            "Worker"
        )
         