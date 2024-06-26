
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

class initFast(FastAPI):
    
    def __init__(self):
        super().__init__()
        origins = [
            "http://127.0.0.1:8000",
            "http://127.0.0.1:57655",
        ]
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware, allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )