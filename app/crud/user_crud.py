#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:16:16 2023

@author: shbshka
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.database_forms import UserBase
from app.schemas.schemas_forms import UserCreate, UserUpdate


class UserCrud:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, user_id: int):
        db_user = await self.db.get(UserBase, user_id)
        if db_user is None:
            return None
        return db_user

    async def get_by_username(self, username: str):
        db_user = (
            (
                await self.db.execute(select(UserBase).where(UserBase.username == username),
                )
            )
        ).scalars().first()
        if not db_user:
            return None
        return db_user

    async def get_list(self):
        db_users = (await self.db.execute(select(UserBase))).scalars().fetchall()
        return db_users

    async def create(self, user: UserCreate):
        new_user = UserBase(name = user.name,
                        surname = user.surname,
                        date_of_birth = user.date_of_birth,
                        zodiac_sign = user.zodiac_sign,
                        username = user.username,
                        password = user.password)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def update(self, user_id: int, user: UserUpdate):
        db_user = await self.db.get(UserBase, user_id)
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def delete(self, user_id: int):
        db_user = await self.db.get(UserBase, user_id)
        await self.db.delete(db_user)
        await self.db.commit()
