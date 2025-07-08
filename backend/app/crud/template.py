from sqlalchemy.orm import Session
from app.models.template import Template
from app.schemas.template import TemplateCreate, TemplateUpdate

def create_template(db: Session, template: TemplateCreate):
    db_template = Template(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

def get_templates(db: Session):
    return db.query(Template).all()

def get_template(db: Session, template_id: int):
    return db.query(Template).filter(Template.id == template_id).first()

def update_template(db: Session, template_id: int, template_data: TemplateUpdate):
    db_template = get_template(db, template_id)
    if db_template:
        for key, value in template_data.dict().items():
            setattr(db_template, key, value)
        db.commit()
        db.refresh(db_template)
    return db_template

def delete_template(db: Session, template_id: int):
    db_template = get_template(db, template_id)
    if db_template:
        db.delete(db_template)
        db.commit()
        return {"message": "Template deleted"}
    return {"error": "Template not found"}
