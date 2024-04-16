from typing import Optional, List
from pydantic import BaseModel

class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int

#Alpha Models
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

# Beta Models
class Payments(BaseModel):
    Amount: float

class OrderDetails(BaseModel):
    ProductId: int
    Barcode: str
    Quantity: float
    Price: float

class Addresses(BaseModel):
    Billing: str
    Shipping: str

class Order(BaseModel):
    ID: int
    ExternalId: int
    CreatedAt: str
    UpdatedAt: str
    ExternalSource: str
    Addresses: Addresses
    OrderDetails: List[OrderDetails]
    Payments: Payments