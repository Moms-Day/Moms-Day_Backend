# from flasgger import swag_from
from flask import Blueprint, request, Response
from flask_restful import Api

# from app.docs.sample import *
from app.views import BaseResource, json_required, gzipped

api = Api(Blueprint('/sample', __name__))
# api.prefix = '/prefix'


@api.resource('/sample')
class Sample(BaseResource):
    # @swag_from(SAMPLE_POST)
    @gzipped
    @json_required({'name': str, 'age': int})
    def post(self):
        payload = request.json

        if not payload['age']:
            raise self.ValidationError('Age is 0!')

        return self.unicode_safe_json_dumps(payload, 201)


@api.resource('/index')
class Index(BaseResource):
    def get(self):
        return Response('success', 200)

    def post(self):
        a = request.json['a']
        b = request.json['b']

        return {
            'first': a,
            'second': b
        }, 200


@api.resource('/deploy')
class AutoDeploy(BaseResource):
    def get(self):
        return Response('yeah~~~~!!!', 200)
