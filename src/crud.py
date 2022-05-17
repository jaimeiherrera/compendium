from sqlalchemy.orm import Session

from . import models, schemas


def get_demon(db: Session, demon_id: int):
    return db.query(models.Demon).filter(models.Demon.id == demon_id).first()


def get_demon_by_name(db: Session, name: str):
    return db.query(models.Demon).filter(models.Demon.name == name).first()


def get_demons(db: Session, limit: int = 100):
    return db.query(models.Demon).limit(limit).all()


def create_demon(db: Session, demon: schemas.DemonCreate):
    db_demon = models.Demon(
        name=demon.name, description=demon.description, url_image=demon.url_image)
    db.add(db_demon)
    db.commit()
    db.refresh(db_demon)
    return db_demon


def update_demon(db: Session, demon: schemas.DemonCreate, demon_id: int):
    db_demon = get_demon(db, demon_id)
    if db_demon is None:
        return None
    db_demon.name = demon.name
    db_demon.description = demon.description
    db_demon.url_image = demon.url_image
    db.commit()
    db.refresh(db_demon)
    return db_demon
