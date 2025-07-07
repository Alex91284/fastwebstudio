from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_projects():
    return [{"id": 1, "name": "Proyecto de prueba"}]
