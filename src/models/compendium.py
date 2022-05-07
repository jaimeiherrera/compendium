from typing import List, Optional

from pydantic import BaseModel, Field


class CompendiumSchema(BaseModel):
    name: str = Field(...)
    level: int = Field(..., gt=0, lt=100)
    description: str = Field(...)
    lives_in: List[str] = Field(...)
    image: Optional[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Jack Frost",
                "level": "7",
                "lives_in": ["Megami Tensei II", "Shin Megami Tensei", "Shin Megami Tensei III: Nocturne", "Shin Megami Tensei IMAGINE"],
                "image": "https://i.imgur.com/fAMd0W8.png",
            }
        }


class UpdateCompendiumModel(BaseModel):
    name: Optional[str]
    level: Optional[int]
    description: Optional[str]
    lives_in: Optional[List[str]]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Berith",
                "level": "9",
                "lives_in": ["Shin Megami Tensei", "Shin Megami Tensei III: Nocturne", "Shin Megami Tensei IMAGINE", "Shin Megami Tensei V"],
                "image": "https://i.imgur.com/fJ6gAJI.jpg",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
