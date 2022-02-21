from services.wordle_service import wordle_logic
from models.wordle_request import *

from flask import request

def wordle_handler():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'

    json = request.get_json()
    
    wordle_logic(WordleReqBody(json))

def hello():
    return "Hello World!"

