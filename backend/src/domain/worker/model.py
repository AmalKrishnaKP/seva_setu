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

from src.core.session import Base


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
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    # Worker details
    verification_proof = Column(
        String(500)
    )

    is_verified = Column(
        Boolean
    )

    exp_yrs = Column(
        Float,
        nullable=False
    )

    expected_hourly_wage = Column(
        Float,
        nullable=False
    )

    service_radius = Column(
        Integer
    )

    # Rating summary
    average_rating = Column(
        Float
    )

    total_rating = Column(
        Integer
    )