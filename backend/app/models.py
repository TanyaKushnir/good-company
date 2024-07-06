from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    edited_date = Column(DateTime, default=datetime.utcnow)
    last_login_date = Column(DateTime)

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    categories = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    edited_date = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))
    managers = relationship('User', secondary='store_managers')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    categories = Column(String)
    store_id = Column(Integer, ForeignKey('stores.id'))
    price = Column(Float)
    amount = Column(Integer)
    max_discount = Column(Float)

class PurchaseHistory(Base):
    __tablename__ = 'purchase_history'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    store_id = Column(Integer, ForeignKey('stores.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    quantity = Column(Integer)
    price = Column(Float)
    purchase_date = Column(DateTime, default=datetime.utcnow)
    shipping_address = Column(String)
    shipping_completed = Column(Boolean, default=False)
    discount = Column(Float)
    payment_method = Column(String)

class Discount(Base):
    __tablename__ = 'discounts'

    id = Column(Integer, primary_key=True, index=True)
    product_ids = Column(String)
    store_ids = Column(String)
    code = Column(String, unique=True)
    expiration_date = Column(DateTime)
    minimum_amount = Column(Float)
    allow_others = Column(Boolean, default=True)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
