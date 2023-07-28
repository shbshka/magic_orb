#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:08:17 2023

@author: shbshka
"""
import uvicorn

import nest_asyncio
nest_asyncio.apply()

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import RedirectResponse, PlainTextResponse
from app.services.services_forms import UserService, PredictionService
from app.crud.prediction_crud import PredictionCrud

from fastapi.templating import Jinja2Templates
import urllib

from app.services.services_forms import PredictionService, UserService

router = APIRouter()

@router.get('/')
async def redirect_to_create():
    return RedirectResponse('prediction/create')


@router.get('prediction/create')
async def create_prediction(request: Request, service: PredictionCrud = Depends(PredictionService.create_prediction)):
    prediction_id, prediction_text = service.create()
    redirect_url = request.url_for('prediction', **{'prediction_id': prediction_id,
                                                    'prediction_text': prediction_text})
    return RedirectResponse(redirect_url)

@router.get('/{prediction_id}')
async def get_prediction(prediction_id: str):
    prediction_text = await PredictionService.get_prediction(PredictionCrud)
    return f'prediction_text: {prediction_text}'

if __name__ == '__main__':
    uvicorn.run(router, host='127.0.0.1', port=8000)
