### Fast API
from fastapi import FastAPI, Security, Response, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer

### Local
from helpers.download import downloadFiles
from helpers.embrapaFiles import embrapaFiles
from database.models import User
from database.database import SessionLocal, engine

#### Auth
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
####


app = FastAPI()

@app.get('/', include_in_schema=False)
async def docs() -> RedirectResponse:
    return RedirectResponse(url='/docs')


## SQLite
#####
#### Authorization

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
origins = [
     "http://127.0.0.1:8000",
]
app.add_middleware(
     CORSMiddleware, allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
          yield db
    finally:
         db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserCreate(BaseModel):
     username: str
     password: str

def get_user_by_username(db: Session, username: str):
     return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    return "complete"

@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
         raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

def authenticate_user(username: str, password: str, db: Session):
     user = db.query(User).filter(User.username == username).first()
     if not user:
          return False
     if not pwd_context.verify(password, user.hashed_password):
          return False
     return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
     to_encode = data.copy()
     if expires_delta:
          expire = datetime.utcnow() + expires_delta
     else:
          expire = datetime.utcnow() + timedelta(minutes=15)
     to_encode.update({"exp": expire})
     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
     return encoded_jwt

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
         raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Incorrect username or password",
              headers={"WWW-Authenticate": "Bearer"},
         )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
         data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Token is invalid or expired")
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Token is invalid or expired")

@app.get("/verify-token/{token}")
async def verify_user_token(token:str):
     verify_token(token=token)
     return {"message": "Token is valid"}

#####


####

@app.get('/getFile/<index>')
def getFile(index, token: str = Depends(oauth2_scheme)):
        embFiles = embrapaFiles()
        fileName = embFiles.getFile(int(index))
        #download embrapa filename
        downloadFile = downloadFiles()
        return downloadFile.download(fileName)
    
@app.get('/getFile')
def getAll():
        embFiles = embrapaFiles()
        for i in range(len(embFiles.files)):
            fileName = embFiles.getFile(i)
            #download embrapa filename
            downloadFile = downloadFiles()
            downloadFile.download(fileName)
        return "end"

####