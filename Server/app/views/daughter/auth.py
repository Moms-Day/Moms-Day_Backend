from flask import Blueprint, request, abort
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from flasgger import swag_from

from app.views import BaseResource, json_required

from app.models.account import DaughterModel

from app.docs.daughter.auth import DAUGHTER_AUTH_POST

api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter'


@api.resource('/auth')
class DaughterAuth(BaseResource):
    @swag_from(DAUGHTER_AUTH_POST)
    @json_required({'id': str, 'pw': str})
    def post(self):
        user = DaughterModel.objects(id=request.json['id']).first()

        return ({
            'accessToken': create_access_token(user.id),
            'refreshToken': create_refresh_token(user.id)
        }, 200) if user and check_password_hash(user.pw, request.json['pw']) else abort(401)
