from flask import Blueprint
from flask_restful import Api
from api.resources import RootResource, UserResource


root_bp = Blueprint("root", __name__, url_prefix='')
api_bp = Blueprint("api", __name__, url_prefix='/api/v1')

root = Api(root_bp)
api = Api(api_bp)

root.add_resource(RootResource, '/')


api.add_resource(UserResource, '/users')


intail=