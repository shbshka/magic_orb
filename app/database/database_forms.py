#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:00:11 2023

@author: shbshka
"""
from pydantic.types import UUID4
from sqlalchemy import Column, ForeignKey, String, Integer, Date
from sqlalchemy.orm import relationship
from app.database.database import Base

class UserBase(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(100))
    date_of_birth = Column(Date)
    zodiac_sign = Column(String)
    username = Column(String(50), unique=True)
    password = Column(String(100))
    predictions = relationship('Prediction',
                               back_populates=list['prediction_text'],
                               cascade='all, delete-orphan')


class PredictionBase(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Column = Column(ForeignKey('users.id'),
                             nullable=False)
    prediction_text = Column(String(100))
