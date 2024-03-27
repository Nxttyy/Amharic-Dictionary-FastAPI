from typing import Union
from fastapi import FastAPI
from db_manager import suggest_words as db_suggest_words, define_word as db_define_word
import json

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Home": "Your Dict Home"}

@app.get("/define")
async def define(word: str):
    definition = db_define_word(word)
    print(definition)
    data = {}
    data['word'], data['en_def'], data['amh_def'] = definition[0], definition[1], definition[2]

    return data

@app.get("/suggest")
async def suggest_words(word: str):
    words = db_suggest_words(word)

    data = {}
    data['words'] = words

    return data
