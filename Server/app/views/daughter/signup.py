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
        'parents': list
    })
    def post(self):
        id = request.json['id']

        if DaughterModel.objects(id=id).first():
            abort(409)

        new_user = {
            'id': id,
            'pw': generate_password_hash(request.json['pw']),
            'phone_number': request.json['phoneNumber'],
            'certify_code': request.json['certifyCode'],
            'name': request.json['name'],
            'age': request.json['age']
        }

        user = DaughterModel(**new_user)

        for parent in request.json['parents']:
            user.parents.append(
                PatientModel(name=parent['name'], age=parent['age'], gender=parent['gender']).save()
            )

        user.save()

        return Response('', 201)
