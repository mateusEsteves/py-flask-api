from flask import Blueprint, jsonify, Response, abort
from middlewares import log_middleware

controller = Blueprint('teste', __name__)


@controller.route('/')
@log_middleware.log_request
def hello_world():
    return 'Hello world!'


@controller.route('/obj')
def get_obj():
    return jsonify(['mateus', 'esteves', 'da silva'])


@controller.route('/bad')
def return_error():
    return Response(status=201)
