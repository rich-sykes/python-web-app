"""FastAPI WebApp"""
import uuid as _uuid
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(
    version="0.0.0",
    title="FastAPI based WebApp!",
    description="Step by step walk through to building a Python web app!",
    contact={"GitHub": "https://github.com/rich-sykes"},
    docs_url=None,
    redoc_url="/",
)


@app.get(
    "/get-request/{name}", description="A simple GET request", summary="GET request"
)
async def root(name: str = "Richard") -> dict:
    """GET request with a query parameter

    Args:
        name (str, optional): A string value, a name for example. Defaults to 'Rich'.

    Returns:
        dict: A personalised message in a dict.
    """
    return {"message": f"Hello {name}"}


class RequestModel(BaseModel):
    name: str = Field(description="Name")
    value_one: float = Field(description="Value One")
    value_two: float | None = Field(description="Value Two")


class ResponseModel(BaseModel):
    uuid: _uuid.UUID = Field(description="UUID")
    name: str = Field(description="Name")
    value_one: str = Field(description="Value One")
    value_two: str = Field(description="Value Two")


@app.post(
    "/post-request/",
    description="A simple POST request",
    summary="POST request",
    response_model=ResponseModel,
)
async def root(item: RequestModel) -> dict:
    """POST request endpoint. This multiplies floats by 10.

    Args:
        item (RequestModel): Request

    Returns:
        dict: Response Message
    """
    output = {
        key: value * 10 if isinstance(value, float) else value
        for (key, value) in item.dict().items()
    }
    output.update({"uuid": _uuid.uuid4()})
    return output


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
