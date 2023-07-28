#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:39:17 2023

@author: shbshka
"""
from transformers import AutoTokenizer, AutoModelWithLMHead
import nltk
from datetime import datetime
import re

def generate_prediction(date, zodiac_sign):
    tokenizer = AutoTokenizer.from_pretrained("stevhliu/astroGPT")
    model = AutoModelWithLMHead.from_pretrained("stevhliu/astroGPT")

    input_ids = tokenizer.encode(date, return_tensors='pt')

    sample_output = model.generate(input_ids,
                                   do_sample=True,
                                   max_length=75,
                                   top_k=20,
                                   top_p=0.97,
                                   pad_token_id=tokenizer.eos_token_id)
    text = ''

    for token in sample_output:
        for token_id in token:
            text += tokenizer.decode(token_id)

    for sentence in nltk.sent_tokenize(text):
        if (not sentence.endswith('.')
            and not sentence.endswith('!')
            and not sentence.endswith('?')):
            text = text.replace(sentence, '')

    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius',
                'Pisces']

    for zodiac in zodiac_signs:
        if zodiac in text:
            text = re.sub(f' *{zodiac} *-* *:*', '', text)


    dates = re.findall(r'[A-Z]\w+\s\d+', text)
    for item in dates:
        if item != date:
            text = re.sub(f'[ ]*{item}[,]*[ ]*[-]*[ ]*', '', text)


    text = re.sub('[ ]*[0-9][,]*[ ]*[-]*[ ]*', '', text)

    text = f'{date}, {zodiac_sign}. {text}'

    return text
