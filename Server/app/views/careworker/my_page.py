import datetime
import base64
import os

from flask import Blueprint, request, Response, abort, current_app
from flask_restful import Api
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import check_password_hash

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel
from app.models.patient import *

from app.docs.careworker.my_page import *

api = Api(Blueprint(__name__, __name__))
api.prefix = '/care/my_page'


@api.resource('')
class MyPage(BaseResource):
    @swag_from(CARE_MY_PAGE_GET)
    @auth_required(CareWorkerModel)
    def get(self):
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()

        return self.unicode_safe_json_dumps({
            'profileImage': care.image_path,
            'name': care.name
        }, 200)


@api.resource('/modify/profile_image')
class ModifyProfileImage(BaseResource):
    @swag_from(CARE_MODIFY_PROFILE_IMAGE_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'encodedImage': str
    })
    def patch(self):
        def convert_and_save(b64_string, path):
            with open(path, "wb+") as fh:
                fh.write(base64.b64decode(b64_string.encode()))

        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        image_path = "./static/imgs/care_worker_profiles/" + str(care.id) + '.jpg'
        conf = current_app.config

        if os.path.isfile(image_path):
            os.remove(image_path)

        convert_and_save(request.json['encodedImage'], image_path)

        care.update(image_path=conf['HOST'] + ":" + conf['PORT'] + image_path[8:])

        return Response('', 201)


@api.resource('/modify/info')
class ModifyAccountInfo(BaseResource):
    @swag_from(CARE_MODIFY_ACCOUNT_INFO_GET)
    @auth_required(CareWorkerModel)
    def get(self):
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        patients = PatientModel.objects(care_worker=care)
        patients_list = [str(patient.name) for patient in patients] if patients else []

        return self.unicode_safe_json_dumps({
            'name': care.name,
            'career': care.career,
            'patients': patients_list,
            'facility_code': care.facility_code,
            'bio': care.bio
        }, 200)

    @swag_from(CARE_MODIFY_ACCOUNT_INFO_PATCH)
    @auth_required(CareWorkerModel)
    def patch(self):
        payload = dict(request.json)
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()

        care.update(**payload)

        return Response('', 201)


@api.resource('/change/password')
class ChangePassword(BaseResource):
    @swag_from(CARE_CHANGE_PASSWORD_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'currentPw': str,
        'newPw': str
    })
    def path(self):
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()

        if not check_password_hash(care.pw, request.json['currentPw']):
            abort(403)

        care.update(pw=request.json['newPw'])

        return Response('', 201)
