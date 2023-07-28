#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:35:41 2023

@author: shbshka
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database.database_forms import PredictionBase, UserBase
from app.schemas.schemas_forms import PredictionCreate

from app.astro_gpt.astrogpt_model import generate_prediction
from datetime import datetime


class PredictionCrud:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, prediction_id: int):
        db_prediction = await self.db.get(PredictionBase, prediction_id)
        if db_prediction is None:
            return None
        return db_prediction

    async def get_by_user_id(self, user_id: str):
        db_predictions = (
            (
                await self.db.execute(select(PredictionBase).where(PredictionBase.user_id == user_id),
                )
            )
        ).scalars().fetchall()
        if not db_predictions:
            return None
        return db_predictions

    async def create(self):
        new_prediction = PredictionBase(
            prediction_text = generate_prediction(
                datetime.now().strftime('%b %d, %Y'),
                UserBase.zodiac_sign)
            )
        self.db.add(new_prediction)
        await self.db.commit()
        await self.db.refresh(new_prediction)

        prediction_id = await self.db.execute(select(PredictionBase.id).where(PredictionBase.prediction_text == new_prediction))

        return prediction_id, new_prediction
