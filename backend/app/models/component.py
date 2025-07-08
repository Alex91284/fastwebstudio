from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # ejemplo: 'text', 'image', 'button'
    content = Column(Text, nullable=True)  # puede variar según el tipo
    order = Column(Integer, nullable=True)  # para el orden en la página
    page_id = Column(Integer, ForeignKey("pages.id"))

    page = relationship("Page", back_populates="components")
