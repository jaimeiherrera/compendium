import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.compendium

demon_collection = database.get_collection("demon_collection")

# helpers


def compendium_helper(demon) -> dict:
    return {
        "id": str(demon["_id"]),
        "name": demon["name"],
        "level": demon["level"],
        "lives_in": demon["course_of_study"],
        "image": demon["image"],
    }


async def retrieve_demons():
    """Retrieve all demons present in the database."""
    demons = []
    async for demon in demon_collection.find():
        demons.append(compendium_helper(demon))
    return demons


async def add_demon(demon_data: dict) -> dict:
    """Add a new demon into to the database

    Args:
        demon_data (dict): the demon data to be added

    Returns:
        dict: inserted demon data
    """
    demon = await demon_collection.insert_one(demon_data)
    new_demon = await demon_collection.find_one({"_id": demon.inserted_id})
    return compendium_helper(new_demon)


async def retrieve_demon(id: str) -> dict:
    """Retrieve a demon with a matching ID

    Args:
        id (str): ID of the demon to be retrieved

    Returns:
        dict: _description_
    """
    demon = await demon_collection.find_one({"_id": ObjectId(id)})
    if demon:
        return compendium_helper(demon)


async def update_demon(id: str, data: dict) -> bool:
    """Update a demon with a matching ID

    Args:
        id (str): ID of the demon to be updated
        data (dict): the new data to be updated

    Returns:
        bool: True if the demon was updated, False otherwise
    """
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    demon = await demon_collection.find_one({"_id": ObjectId(id)})
    if demon:
        updated_demon = await demon_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_demon:
            return True
        return False


async def delete_demon(id: str) -> bool:
    """Delete a demon from the database

    Args:
        id (str): ID of the demon to be deleted

    Returns:
        bool: True if the demon was deleted, False otherwise
    """
    demon = await demon_collection.find_one({"_id": ObjectId(id)})
    if demon:
        await demon_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
