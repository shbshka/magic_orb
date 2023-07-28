#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:47:27 2023

@author: shbshka
"""
from fastapi import HTTPException

from app.crud.user_crud import UserCrud
from app.schemas.schemas_forms import UserCreate, UserUpdate, PredictionCreate
from app.crud.prediction_crud import PredictionCrud

class UserService:
    def __init__(self, crud: UserCrud):
        self.crud = crud

    async def get_users(self):
        db_users = await self.crud.get_list()
        return db_users

    async def get_user(self, user_id: int):
        db_user = await self.crud.get(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return db_user

    async def create_user(self, user: UserCreate):
        db_user = await self.crud.get_by_username(username=user.username)
        if db_user:
            raise HTTPException(
                status_code=400,
                detail='This username is not available'
                )
        return await self.crud.create(user=user)

    async def update_user(self, user_id: int, user: UserUpdate):
        db_user = await self.crud.get(user_id=user_id)
        if db_user is None:
            raise HTTPException(
                status_code=404,
                detail='User not found'
                )
        updated_user = await self.crud.update(user_id=user_id, user=user)
        return updated_user

    async def delete_user(self, user_id: int):
        db_user = await self.crud.get(user_id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail='User not found')
        await self.crud.delete(user_id=user_id)
        return {'status': 'true', 'message': 'The user has been deleted'}


class PredictionService:
    def __init__(self, crud: PredictionCrud):
        self.crud = crud

    async def get_prediction(self):
        db_prediction = await self.crud.get()
        if db_prediction is None:
            raise HTTPException(status_code=404, detail='Prediction not found')
        return db_prediction

    async def get_predictions(self, user_id: int):
        db_predictions = await self.crud.get_by_user_id(user_id=user_id)
        if db_predictions is None:
            raise HTTPException(
                status_code=404,
                detail='Prediction not found'
                )

    async def create_prediction(self):
        return await self.crud.create()
