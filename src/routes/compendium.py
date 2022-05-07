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


@router.get("/", response_description="Demons retrieved")
async def get_demons():
    demons = await retrieve_demons()
    if demons:
        return ResponseModel(demons, "Demons data retrieved successfully")
    return ResponseModel(demons, "Empty list returned")


@router.get("/{id}", response_description="Demon data retrieved")
async def get_demon_data(id):
    demon = await retrieve_demon(id)
    if demon:
        return ResponseModel(demon, "Demon data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Demon doesn't exist.")


@router.put("/{id}")
async def update_demon_data(id: str, req: UpdateCompendiumModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_demon = await update_demon(id, req)
    if updated_demon:
        return ResponseModel(
            "Demon with ID: {} name update is successful".format(id),
            "Demon name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the demon data.",
    )


@router.delete("/{id}", response_description="Demon data deleted from the database")
async def delete_demon_data(id: str):
    deleted_demon = await delete_demon(id)
    if deleted_demon:
        return ResponseModel(
            "Demon with ID: {} removed".format(
                id), "Demon deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Demon with id {0} doesn't exist".format(
            id)
    )
