from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .user import User

from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    url = Column(String, nullable=True)

    # 🔑 Relación con usuario
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relación inversa hacia User
    user = relationship("User", back_populates="projects")

    # Relación con páginas y sitios
    pages = relationship("Page", back_populates="project", cascade="all, delete-orphan")
    site = relationship("Site", back_populates="project")

