#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:07:09 2023

@author: shbshka
"""
from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    name: str
    surname: str
    date_of_birth: date
    zodiac_sign: str
    username: str
    password: str
    predictions: list


class UserCreate(UserBase):
    name: str
    surname: str
    date_of_birth: date
    zodiac_sign: str
    username: str
    password: str
    predictions: list


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    class Config:
        orm_mode = True


class UserGet(UserInDB):
    id: str
    name: str
    surname: str
    date_of_birth: date
    zodiac_sign: str
    username: str
    password: str
    predictions: list


class PredictionsBase(BaseModel):
    prediction_text: str


class PredictionCreate(PredictionsBase):
    prediction_text: str


class PredictionInDB(PredictionsBase):
    class Config:
        orm_mode = True


class PredictionGet(PredictionInDB):
    id: str
    user_id: str
    prediction_text: str
