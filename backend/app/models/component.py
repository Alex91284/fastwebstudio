from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(40), nullable=False)  # ejemplo: 'text', 'image', 'button'
    content = Column(Text, nullable=True)  # puede variar según el tipo
    order = Column(Integer, default=0)  # para el orden en la página
    parent_id = Column(Integer, ForeignKey("components.id"), nullable=True)

    props = Column(JSON, nullable=False, default=dict)   # contenido (ej. text, src, href)
    styles = Column(JSON, nullable=False, default=dict)  # estilos inline (ej. { color, fontSize })


    page_id = Column(Integer, ForeignKey("pages.id"), nullable=False)

    page = relationship("Page", back_populates="components")
    children = relationship("Component", cascade="all,delete-orphan")
