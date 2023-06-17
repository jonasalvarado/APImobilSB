from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from app.auth.jwt import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from uuid import uuid4
from app.routers import marcas
from app.routers import users
from sqlalchemy.orm import Session
from app.models import models, schemas
from app.db.database import SessionLocal, engine

app = FastAPI()


# Dependency install on digitalocean 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(marcas.router)
app.include_router(users.router)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to subicicleta mobil API!"}

@app.post('/login', summary="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    # user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email "
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect  password"
        )
  
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }