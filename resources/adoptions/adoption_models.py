from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class AdoptionModel(BaseModel):
    adoptionId: str
    petId: str
    adopterId: str
    status: str
    createdAt: str
    updatedAt: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "adoptionId": "aid_0001",
                    "petId": "pid_0001",
                    "adopterId": "uid_0001",
                    "status": "pending",
                    "createdAt": "2023-10-18",
                    "updatedAt": "",
                }
            ]
        }
    }


class AdoptionRspModel(AdoptionModel):
    links: List[Link] = None