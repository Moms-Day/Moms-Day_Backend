from flask import Blueprint, request, abort
from flask_restful import Api
from werkzeug.security import check_password_hash
from flasgger import swag_from
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

from app.views import BaseResource, json_required

from app.models.account import CareWorkerModel

from app.docs.careworker.auth import CARE_AUTH_POST


api = Api(Blueprint(__name__, __name__))
api.prefix = '/care'


@api.resource('/auth')
class CareAuth(BaseResource):
    @swag_from(CARE_AUTH_POST)
    @json_required({'id': str, 'pw': str})
    def post(self):
        user = CareWorkerModel.objects(id=request.json['id']).first()

        return ({
            'accessToken': create_access_token(user.id),
            'refreshToken': create_refresh_token(user.id)
        }, 200) if user and check_password_hash(user.pw, request.json['pw']) else abort(401)


@api.resource('/refresh')
class TokenRefresh(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        if not CareWorkerModel.objects(id=get_jwt_identity()).first():
            abort(401)

        return {
            'accessToken': create_access_token(get_jwt_identity())
        }, 200


# @api.resource('/test')
# class TestReload(BaseResource):
#     def post(self):
#         care = CareWorkerModel.objects(id=request.json['id']).first()
#
#         for k, v in dict(care.to_mongo()).items():
#             print('{} : {}'.format(str(k), str(v)))
#
#         a = [{k: v} for k, v in dict(care.to_mongo()).items() if type(v) == int and v == 3]
#         print(a)
#
#         return '', 201
