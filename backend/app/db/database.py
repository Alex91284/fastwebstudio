from app.db.session import Base, engine
from app.models import user, project, page, component, template, site

def create_tables():
    Base.metadata.create_all(bind=engine)
