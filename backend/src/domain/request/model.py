import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Request(Base):
    __tablename__ = "request"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    job_id = Column(
        UUID(as_uuid=True),
        ForeignKey("job.id"),
        nullable=False
    )

    worker_id = Column(
        UUID(as_uuid=True),
        ForeignKey("worker.id"),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=True
    )

    requested_at = Column(
        DateTime,
        nullable=True
    )

    responded_at = Column(
        DateTime,
        nullable=True
    )

    job = relationship(
        "Job",
        back_populates="requests"
    )

    worker = relationship(
        "Worker",
        back_populates="requests"
    )