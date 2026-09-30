import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    UUID,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from src.core.session import Base

class Favorite(Base):
    __tablename__="favorites"
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,

    )
    worker_id=Column(
        UUID(as_uuid=True),
        ForeignKey("workers.id",ondelete="CASCADE"),
        nullable=False,
    )
    customer_id=Column(
        UUID(as_uuid=True),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
    )
    created_at=Column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc),
    )
    #Relationship
    worker=relationship(
        "Worker",
        back_populates="favorites"
                        )
    customer=relationship("User")

    __table_args__=(
        UniqueConstraint("worker_id", "customer_id",name="uq_worker_customer_favorite"),
    )