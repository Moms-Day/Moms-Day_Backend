from flask import Blueprint, request, Response
from flask_restful import Api
from werkzeug.security import generate_password_hash
from flasgger import swag_from

from app.views import BaseResource, json_required

from app.models.account import CareWorkerModel

from app.docs.careworker.signup import SIGNUP_POST

api = Api(Blueprint(__name__, __name__))
api.prefix = '/care'


@api.resource('/signup')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    @json_required({
        'id': str,
        'pw': str,
        'name': str,
        'career': int,
        'patientInCharge': int,
        'phoneNumber': str,
        'certifyCode': str,
        'facilityCode': str,
        'bio': str
    })
    def post(self):
        id = request.json['id']
        new_user = {
            'id': id,
            'pw': generate_password_hash(request.json['pw']),
            'name': request.json['name'],
            'career': request.json['career'],
            'patient_in_charge': request.json['patientInCharge'],
            'phone_number': request.json['phoneNumber'],
            'certify_code': request.json['certifyCode'],
            'facility_code': request.json['facilityCode'],
            'bio': request.json['bio']
        }

        # profile_image = request.files['image']

        if CareWorkerModel.objects(id=id).first():
            return {
                'msg': 'id duplicated'
            }, 409

        CareWorkerModel(**new_user).save()

        return Response('', 201)
