from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    url = Column(String, nullable=True)

    # 🔑 Relación con usuario
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relación con páginas y sitios
    pages = relationship("Page", back_populates="project", cascade="all, delete-orphan")
    sites = relationship("Site", back_populates="project")

    # Relación inversa hacia User
    user = relationship("User", back_populates="projects")
