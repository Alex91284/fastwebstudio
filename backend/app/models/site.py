from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    slug = Column(String(160), unique=True, index=True)
    is_published = Column(Boolean, default=False)
    published_at = Column(DateTime, nullable=True)
    domain = Column(String, unique=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), unique=True, nullable=False)

    project = relationship("Project", back_populates="sites")

    __table_args__ = (UniqueConstraint("slug", name="uq_site_slug"),)
