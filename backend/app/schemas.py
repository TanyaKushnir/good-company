from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_date: datetime
    edited_date: datetime
    last_login_date: Optional[datetime]

    class Config:
        orm_mode = True

class StoreBase(BaseModel):
    name: str
    description: str
    categories: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    created_date: datetime
    edited_date: datetime
    owner_id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    categories: str
    price: float
    amount: int
    max_discount: float

class ProductCreate(ProductBase):
    store_id: int

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class PurchaseHistoryBase(BaseModel):
    product_id: int
    store_id: int
    user_id: int
    quantity: int
    price: float
    shipping_address: str
    shipping_completed: bool
    discount: float
    payment_method: str

class PurchaseHistoryCreate(PurchaseHistoryBase):
    pass

class PurchaseHistory(PurchaseHistoryBase):
    id: int
    purchase_date: datetime

    class Config:
        orm_mode = True

class DiscountBase(BaseModel):
    product_ids: str
    store_ids: str
    code: str
    expiration_date: datetime
    minimum_amount: float
    allow_others: bool

class DiscountCreate(DiscountBase):
    pass

class Discount(DiscountBase):
    id: int

    class Config:
        orm_mode = True

class AddressBase(BaseModel):
    address: str
    city: str
    country: str
    user_id: int

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
