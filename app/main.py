from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

from app.models import user, task
from app.routes import auth, tasks


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API is working 🚀"}
