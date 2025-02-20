from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.models import Base
from routers.main import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="myfont_api",
    docs_url=None, redoc_url=None, openapi_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def myfont():
    return {"message": "welcome to myfont!"}

app.include_router(router, prefix="/api/v1")