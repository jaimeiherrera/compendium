from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.post("/demons/", response_model=schemas.Demon, tags=["Demons"])
def create_demon(demon: schemas.DemonCreate, db: Session = Depends(get_db)):
    db_demon = crud.get_demon_by_name(db, name=demon.name)
    if db_demon:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_demon(db=db, demon=demon)


@app.get("/demons/", response_model=list[schemas.Demon], tags=["Demons"])
def read_demons(limit: int = 100, db: Session = Depends(get_db)):
    demons = crud.get_demons(db, limit=limit)
    return demons


@app.get("/demons/{demon_id}", response_model=schemas.Demon, tags=["Demons"])
def read_demon(demon_id: int, db: Session = Depends(get_db)):
    db_demon = crud.get_demon(db, demon_id=demon_id)
    if db_demon is None:
        raise HTTPException(status_code=404, detail="Demon not found")
    return db_demon
