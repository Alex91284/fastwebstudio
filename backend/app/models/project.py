from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    url = Column(String, nullable=True)

    # Relación con páginas
    pages = relationship("Page", back_populates="project", cascade="all, delete-orphan")
