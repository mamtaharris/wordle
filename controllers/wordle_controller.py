from services.wordle_service import wordle_logic
from flask import  request, jsonify, make_response


from flask import request

def wordle_handler():
    reqBody = request.get_json()
    if 'word' not in reqBody:
        return make_response(jsonify({'error': 'missing word in request'}), 400)
    return wordle_logic(reqBody)

def hello():
    return "Hello, Welcome to my Wordle"

