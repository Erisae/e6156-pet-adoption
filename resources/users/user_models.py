from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class UserModel(BaseModel):
    userId: str
    username: str
    email: str
    passwordHash: str
    userType: str
    createdAt: str
    updatedAt: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "userId": "uid0001",
                    "username": "Alexa",
                    "passwordHash": "xxxxxxxxx",
                    "userType": "adpoter",
                    "createdAt": "2023=10-18",
                    "updatedAt": ""
                },
                {
                    "userId": "uid0002",
                    "username": "Wammy's house",
                    "passwordHash": "xxxxxxxxx",
                    "userType": "shelter",
                    "createdAt": "2023=10-18",
                    "updatedAt": ""
                }
            ]
        }
    }


class UserRspModel(UserModel):
    links: List[Link] = None