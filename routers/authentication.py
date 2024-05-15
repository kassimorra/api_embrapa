from fastapi import APIRouter, HTTPException
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import authentication as auth

router = APIRouter(
    prefix="/auth"
)

@router.post("/register", status_code=status.HTTP_201_CREATED, tags=["Authentication"])
async def register_user(user: auth.UserCreate, db: Session = Depends(auth.get_db)):
    """
    Registra o usuário no banco passando Usuário e Password no formato JSON
    """
    db_user = auth.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return auth.create_user(db=db, user=user)

@router.post("/token", status_code=status.HTTP_201_CREATED, tags=["Authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(auth.get_db)):
    """
    Rota padrão de autenticação utilizando usuário e senha
    """
    user = auth.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/verify-token/{token}", tags=["Authentication"])
async def verify_user_token(token:str):
    """
    Verifica se o token informado é válido, inválido ou expirado
    """    
    auth.verify_token(token=token)
    return {"message": "Token is valid"}