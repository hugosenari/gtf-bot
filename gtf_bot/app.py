import json
from bottle import default_app, get, post, request
from .bot import handler

@get('/')
def get():
    return '[]'

@post('/')
def post():
    body = request.body.read()
    handler(body.decode('utf-8'))
    return '[]'

app = default_app()
