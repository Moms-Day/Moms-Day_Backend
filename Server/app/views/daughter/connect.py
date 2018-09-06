import re
import uuid

from flask import Blueprint, request, Response
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource, json_required, auth_required

from app.models.facility import FacilityModel
from app.models.account import CareWorkerModel, DaughterModel
from app.models.connect import RequestModel

from app.docs.daughter.connect import DAUGHTER_SEARCH_FOR_CONNECTION_GET, DAUGHTER_REQUEST_CONNECTION_POST


api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/connect'


@api.resource('/search')
class SearchFacility(BaseResource):
    @auth_required(DaughterModel)
    @swag_from(DAUGHTER_SEARCH_FOR_CONNECTION_GET)
    def get(self):
        name = request.args.get('facilityName')
        facs = FacilityModel.objects(name=re.compile(str('.*' + name + '.*')))

        data = [{
            'facilityCode': fac.facility_code,
            'name': fac.name,
            'address': fac.address,
            'careWorkers': [{
                'id': care.id,
                'name': care.name
            } for care in CareWorkerModel.objects(facility_code=fac.facility_code)]
        } for fac in facs] if facs else []

        return self.unicode_safe_json_dumps(data, 200)


@api.resource('/request')
class RequestConnection(BaseResource):
    @auth_required(DaughterModel)
    @swag_from(DAUGHTER_REQUEST_CONNECTION_POST)
    @json_required({
        'careId': str,
        'requesterId': str,
        'requesterName': str,
        'patientName': str,
        'patientAge': int,
        'patientGender': bool
    })
    def post(self):
        req_id = str(uuid.uuid4())
        payload = request.json

        RequestModel(
            req_id=req_id,
            care_worker=CareWorkerModel.objects(id=payload['careId']).first(),
            requester_id=payload['requesterId'],
            requester_name=payload['requesterName'],
            patient_name=payload['patientName'],
            patient_age=payload['patientAge'],
            patient_gender=payload['patientGender']
        ).save()

        return Response('', 201)


@api.resource('/plus')
class InsertDummyData(BaseResource):
    def post(self):
        FacilityModel(
            facility_code=request.json['facilityCode'],
            name=request.json['name'],
            phone_number=request.json['phoneNumber'],
            address=request.json['address'],
            bio=request.json['bio'],
            image_path=request.json['imagePath']
        ).save()

        return '', 201


@api.resource('/plus2')
class InsertDummyDataCare(BaseResource):
    def post(self):
        CareWorkerModel(
            id=request.json["id"],
            pw=request.json["pw"],
            phone_number=request.json['phoneNumber'],
            name=request.json["name"],
            facility_code=request.json["facilityCode"],
            career=request.json["career"],
            patient_in_charge=request.json["patientInCharge"],
            bio=request.json["bio"]
        ).save()

        return '', 201
