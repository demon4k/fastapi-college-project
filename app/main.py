from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(title="FastAPI College Project")

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "FastAPI CRUD project is working"}