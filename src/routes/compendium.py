from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.database import (add_demon, delete_demon, retrieve_demon,
                          retrieve_demons, update_demon)
from src.models.compendium import (CompendiumSchema, ErrorResponseModel,
                                   ResponseModel, UpdateCompendiumModel)

router = APIRouter()


@router.post("/", response_description="Demon data added into the database")
async def add_demon_data(demon: CompendiumSchema = Body(...)):
    demon = jsonable_encoder(demon)
    new_demon = await add_demon(demon)
    return ResponseModel(new_demon, "Demon added successfully.")
