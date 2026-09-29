import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from src.core.session import Base

class Badge(Base):
    __tablename__="badges"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name = Column(
        String(100),
        nullable=False,
        unique=True,
    )
    description = Column(
        Text,
        nullable=True,
    )
    threshold = Column(
        Integer,
        nullable=True,
    )
    terms = Column(
        Text,
        nullable=True,
    )
    icon_url = Column(
        Text,
        nullable=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc),
        onupdate=lambda:datetime.now(timezone.utc),
    )

    #Relationships
    worker_badges = relationship(
        "WorkerBadge",
        back_populates="badge",
        cascade="all, delete-orphan"
    )

class WorkerBadge(Base):
    __tablename__="worker_badges"

    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    worker_id = Column(
        UUID(as_uuid=True),
        ForeignKey("workers.id",ondelete="CASCADE"),
        nullable=False,
    )
    badge_id=Column(
        UUID(as_uuid=True),
        ForeignKey("badges.id",ondelete="CASCADE"),
        nullable=False,
    )
    awarded_at=Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    #Relationships
    badge = relationship("Badge", back_populates="worker_badges")
    worker = relationship("Worker")

    __table_args__=(
        UniqueConstraint("worker_id", "badge_id", name="uq_worker_badge"),
    )
