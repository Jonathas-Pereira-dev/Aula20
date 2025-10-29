from pydantic import BaseModel, PositiveFloat, EmailStr, validators,Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


