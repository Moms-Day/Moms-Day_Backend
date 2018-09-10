import datetime
import base64
import os

from flask import Blueprint, request, Response, abort, current_app
from flask_restful import Api
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import check_password_hash

from app.views import BaseResource, json_required, auth_required

from app.models.account import DaughterModel
from app.models.patient import *

from app.docs.daughter.my_page import *

api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/my_page'


# @api.resource('')
# class MyPage(BaseResource):
#     @auth_required(DaughterModel)
#     def get(self):
#         daughter = DaughterModel.objects(id=get_jwt_identity()).first()
#
#         return self.unicode_safe_json_dumps({
#             'name': daughter.name
#         }, 200)


@api.resource('/account_info')
class ViewAccountInfo(BaseResource):
    @swag_from(DAUGHTER_VIEW_ACCOUNT_INFO_GET)
    @auth_required(DaughterModel)
    def get(self):
        daughter = DaughterModel.objects(id=get_jwt_identity()).first()
        patients = PatientModel.objects(daughter=daughter)

        return self.unicode_safe_json_dumps({
            'name': daughter.name,
            'age': daughter.age,
            'patients': [{
                'name': str(patient.name),
                'age': patient.age,
                'gender': patient.gender
            } for patient in patients] if patients else []
        }, 200)


@api.resource('/change/password')
class ChangePassword(BaseResource):
    @swag_from(DAUGHTER_CHANGE_PASSWORD_PATCH)
    @auth_required(DaughterModel)
    @json_required({
        'currentPw': str,
        'newPw': str
    })
    def path(self):
        daughter = DaughterModel.objects(id=get_jwt_identity()).first()

        if not check_password_hash(daughter.pw, request.json['currentPw']):
            abort(403)

        daughter.update(pw=request.json['newPw'])

        return Response('', 201)


@api.resource('/withdraw')
class WithDraw(BaseResource):
    @swag_from(DAUGHTER_WITHDRAW_DELETE)
    @auth_required(DaughterModel)
    @json_required({
        'pw': str
    })
    def delete(self):
        daughter = DaughterModel.objects(id=get_jwt_identity()).first()

        if not check_password_hash(daughter.pw, request.json['pw']):
            abort(403)

        daughter.delete()

        return Response('', 200)
