import os

from flask import Blueprint, Response
from flask_restful import Api
from app.views import BaseResource

api = Api(Blueprint(__name__, __name__))


@api.resource('/hook')
class GetHookEvent(BaseResource):
    def post(self):
        os.system('. ../hook.sh')

        return Response('hook!', 200)
