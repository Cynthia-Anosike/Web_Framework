#!/usr/bin/env python3
""" A sqlachemy db management with attributes
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class User(Base):
    """ Declared a user's personal information"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    hashed_password = Column(String(20), nullable=False)
    session_id = Column(String(100)
