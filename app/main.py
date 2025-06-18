from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registro")
def crear_registro(registro: schemas.RegistroCreate, db: Session = Depends(get_db)):
    db_registro = models.Registro(name=registro.name)
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return {"mensaje": f"Registro guardado para {registro.name}"}
