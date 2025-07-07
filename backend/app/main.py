from fastapi import FastAPI
from app.db.database import engine, Base

from app.models import user, project, page
from app.routes import users, projects, pages
from app.db.session import engine
from app.db.database import create_tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastWebStudio API")

@app.on_event("startup")
def startup():
    create_tables()

# Incluir routers con prefijos
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(pages.router, prefix="/api/pages", tags=["Pages"])

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a FastWebStudio API 🚀"}
