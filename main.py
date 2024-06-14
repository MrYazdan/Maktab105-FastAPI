from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
items = []


class Item(BaseModel):
    id: int = Field(default_factory=lambda: len(items))
    name: str
    price: float
    is_offer: bool = False


@app.get("/items")
@app.get("/items/{item_id}")
def read_item(item_id: int | None = None, key: Union[str, None] = None):
    if item_id:
        return items[item_id-1] if not key else getattr(items[item_id-1], key)
    return items


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item.model_dump()
