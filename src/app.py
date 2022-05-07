from fastapi import FastAPI

from src.routes.compendium import router as CompendiumRouter

app = FastAPI()

app.include_router(CompendiumRouter, tags=["Compendium"], prefix="/compendium")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
