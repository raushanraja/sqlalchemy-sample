from uuid import uuid4

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from ..core.base_class import Base


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, unique=True, nullable=False)
    email= Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())