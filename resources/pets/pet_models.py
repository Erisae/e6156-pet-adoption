from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class PetModel(BaseModel):
    petId: str
    shelterId: str
    petname: str
    specie: str
    breed: str
    age: str
    healthRecords: str
    images: str
    createdAt: str
    updatedAt: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "petId": "pid_0001",
                    "shelterId": "uid_0002",
                    "petname": "LLawliet",
                    "specie": "dog",
                    "breed": "German Shepherd",
                    "age": "1.3",
                    "healthRecords": "GOOD",
                    "images": " ",
                    "createdAt": "2023-10-18",
                    "updatedAt": "2023-10-18"
                }
            ]
        }
    }


class PetRspModel(PetModel):
    links: List[Link] = None