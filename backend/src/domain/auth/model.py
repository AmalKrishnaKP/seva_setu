from datetime import datetime, timezone
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, UUID
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import relationship

from src.core.session import Base


class UserSession(Base):
    __tablename__="sessions"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    refresh_token_hash = Column(
        String(255),
        nullable=False,
        unique=True,
    )

    user_agent = Column(
        String(512),
    )

    ip_address = Column(
        INET,
    )

    expires_at = Column(
        DateTime(timezone=True),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    last_used_at = Column(
        DateTime(timezone=True),
    )

    revoked_at = Column(
        DateTime(timezone=True),
    )

    user = relationship(
        "User",
        back_populates="sessions",
    )

    
