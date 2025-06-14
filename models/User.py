from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)  
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    summaries = relationship("Summary", back_populates="user")