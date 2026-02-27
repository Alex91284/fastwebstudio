from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import UniqueConstraint

class Page(Base):
    __tablename__ = "pages"
    __table_args__ = (
        UniqueConstraint("project_id", "slug", name="uix_slug_project"),
    )

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    slug = Column(String(160),  nullable=False)
    content = Column(Text, nullable=True)
    order = Column(Integer, default=0)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    
    project = relationship("Project", back_populates="pages")
    components = relationship("Component", back_populates="page", cascade="all, delete-orphan")
