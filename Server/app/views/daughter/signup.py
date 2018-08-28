from flask import Blueprint, request, Response, abort
from flask_restful import Api
from werkzeug.security import generate_password_hash
from flasgger import swag_from

from app.views import BaseResource, json_required

from app.models.account import DaughterModel
from app.models.patient import PatientModel

from app.docs.daughter.signup import DAUGHTER_SIGNUP_POST

api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter'


@api.resource('/signup')
class DaughterSignup(BaseResource):
    @swag_from(DAUGHTER_SIGNUP_POST)
    @json_required({
        'id': str,
        'pw': str,
        'phoneNumber': str,
        'name': str,
        'age': int,
    })
    def post(self):
        id = request.json['id']

        if DaughterModel.objects(id=id).first():
            abort(409)

        req = request.json

        new_user = {
            'id': id,
            'pw': generate_password_hash(req['pw']),
            'phone_number': req['phoneNumber'],
            'certify_code': req['certifyCode'],
            'name': req['name'],
            'age': req['age']
        }

        d = DaughterModel(**new_user).save()

        if req['p_name']:
            PatientModel(name=req['p_name'], age=req['p_age'], gender=req['p_gender'], daughter=d).save()

        return Response('', 201)
