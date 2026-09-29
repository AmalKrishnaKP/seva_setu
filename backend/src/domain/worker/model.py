import uuid

from sqlalchemy import (
    Column,
    UUID,
    String,
    Float,
    Boolean,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from core.session import Base


class Worker(Base):
    __tablename__ = "workers"

    # Identity
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # User relationship
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )


    expected_hourly_wage = Column(
        Float,
        nullable=False
    )

    # Rating summary
    average_rating = Column(
        Float,
        default=0.0
    )

    total_rating = Column(
        Integer,
        default=0
    )

    # Relationship
    user = relationship(
        "User",
        back_populates="worker"
    )