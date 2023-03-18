from flask_restful import Resource, Api
from flask import request
from .. import shop

api = Api(shop)

class IndexResource(Resource):
    def get(self):
        context = {
            'status': True,
            'content': 'Api Rest Activo'
        }
        
        return context
    
api.add_resource(IndexResource, '/')