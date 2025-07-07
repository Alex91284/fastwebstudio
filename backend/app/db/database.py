from app.db.session import Base, engine
from app.models import user

def create_tables():
    Base.metadata.create_all(bind=engine)
