from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.models import user, project, page, component, template, site

from app.routes import users, projects, pages, components, templates, auth,sites
from app.db.session import engine
from app.db.database import create_tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastWebStudio API")

origins = [
    "http://localhost:5173",  # frontend Vite
    "http://127.0.0.1:5173",  # por si usas localhost o 127.0.0.1
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_tables()

# Incluir routers con prefijos
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(projects.router, prefix="/api", tags=["Projects"])
app.include_router(pages.router, prefix="/api", tags=["Pages"])
app.include_router(components.router, prefix="/api", tags=["Components"])
app.include_router(templates.router, prefix="/api", tags=["Templates"])
app.include_router(auth.router, prefix="", tags=["Auth"])
app.include_router(sites.router, prefix="/api", tags=["Site"])

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a FastWebStudio API 🚀"}

@app.options("/{full_path:path}")
def preflight_handler(full_path: str):
    return {}