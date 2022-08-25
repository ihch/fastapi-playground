import datetime
from enum import Enum
import json

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost', "http://localhost:3000"]
)


class Type(Enum):
    JSON = 1
    YAML = 2
    PLAIN = 3


class Message(BaseModel):
    message: str
    date: datetime.datetime
    type: Type


@app.get("/", response_model=Message)
async def root():
    return {
        "message": "Hello, World!",
        "date": datetime.datetime.now(),
        "type": Type.JSON
    }


def export_openapi_scheme():
    with open('openapi/openapi.json', 'w') as file:
        json.dump(get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ), file)


export_openapi_scheme()
