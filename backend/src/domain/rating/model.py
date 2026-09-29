import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, String,DateTime, Index,Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.core.session import Base
from datetime import datetime,timezone


class Rating(Base):
    __tablename__="rating"
    id=Column(
        UUID(as uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id=Column(
        UUID(as_uuid=True),
        ForeignKey("user_id",ondelete="CASCADE"),
        Nullable=False
    )

    job_id=Column(
        UUID(as_uuid=True),
        ForiegnKey("job_id",ondelete="CASCADE"),
        Nullable=False
    )

    worker_id=Column(
        UUID(as_uuid=True),
        ForeignKey("woker_id",ondelete="CASCADE"),
        Nullable=False
    )

    rating=Column(
        integer,
        Nullable=False
    )

    feedback=Column(
        string(255)
        Nullable=True
    )

    created_at=Column(
        DateTime,
        default=datetime.now(timezone.utc)

    )


    job = relationship(
        "Job"
        back_populates="rating"
    )

    customer = relationship(
        "Customer"
        back_populates="rating"
    )

        worker = relationship(
        "Worker"
        back_populates="rating"
    )