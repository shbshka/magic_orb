#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:44:21 2023

@author: shbshka
"""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

Base = declarative_base()
engine = create_async_engine(settings.POSTGRES_URL, future=True)


async def get_session() -> AsyncSession:
    """
    The get_session function is a factory function that creates an instance
    of the AsyncSession class. The AsyncSession class inherits from the Session
    class and adds functionality to it. This allows us to use async with
    statements in order to create asynchronous sessions, which are used by our
    database models.
    """
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session
