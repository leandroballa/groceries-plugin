from typing import Optional, List
from pydantic import BaseModel

class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int

class Size(BaseModel):
    size_id: int
    size_code: str
    size_name: str
    price: float
    barcode: str

class Colour(BaseModel):
    colour_id: int
    colour_code: str
    colour_name: str
    sizes: List[Size]

class Product(BaseModel):
    style_id: int
    style_code: str
    name: str
    colours: List[Colour]