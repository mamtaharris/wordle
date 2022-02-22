from services.wordle_service import wordle_logic
from models.wordle_request import *
from models.error_response import *
from flask import Flask, request, jsonify, make_response


from flask import request

def wordle_handler():
    json = request.get_json()
    
    return make_response( jsonify(wordle_logic(WordleReqBody(json))), 200)

def hello():
    return "Hello World!"

