import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, String,DateTime, Index,Integer,ForeignKey,Enum
from sqlalchemy.orm import relationship
from src.core.session import Base
from datetime import datetime,timezone
from core.enum import AuditTagEnum



class Audit(Base):
    __tablename__="audit"
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    user_id=Column(
        UUID(as_uuid=True),
        ForiegnKey("user_id",ondelete="CASCADE"),
        Nullable=False
    )

    description=Column(
        string(225),
        Nullable=False

    )

    tag=Column(
        Enum(AuditTagEnum),
        Nullable=False
    )


    user = relationship(
        "User"
        back_populates="Audit"
    )


