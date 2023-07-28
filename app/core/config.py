#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:45:27 2023

@author: shbshka
"""
import os

from dotenv import load_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.networks import PostgresDsn

BASEDIR: str = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
)
load_dotenv(os.path.join(BASEDIR, ".env"))


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Magic Orb'
    SERVER_NAME: str = os.getenv('SERVER_NAME', default='localhost')

    # PostgreSQL database settings
    PG_DB_NAME: str = os.getenv("DB_NAME", default="postgres")
    PG_USER: str = os.getenv("POSTGRES_USER", default="postgres")
    PG_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", default="postgres")
    PG_DB_HOST: str = os.getenv("DB_HOST", default="localhost")
    PG_DB_PORT: str = os.getenv("DB_PORT", default="5432")
    POSTGRES_URL: str = PostgresDsn.build(
        scheme="postgresql+asyncpg",
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_DB_HOST,
        port=PG_DB_PORT,
        path=f"/{PG_DB_NAME}",
    )


settings = Settings()
