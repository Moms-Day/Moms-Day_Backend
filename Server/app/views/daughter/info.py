from flask import Blueprint, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource

from app.models.facility import FacilityModel
from app.models.account import CareWorkerModel

from app.docs.daughter.info import *


api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/info'


@api.resource('/facility/<facility_code>')
class ShowParticularFacility(BaseResource):
    @swag_from(DAUGHTER_SHOW_FACILITY_INFO_GET)
    def get(self, facility_code):
        fac_info = FacilityModel.objects(facility_code=facility_code).first()

        if not fac_info:
            abort(400)

        def get_average_value(val):
            return round(val / fac_info.evaluation_count, 1) if fac_info.evaluation_cost != 0 else 0

        one_line_e = [e for e in fac_info.one_line_evaluation]

        return {
            'imagePath': fac_info.image_path,
            'name': fac_info.name,
            'phoneNumber': fac_info.phone_number,
            'address': fac_info.address,
            'bio': fac_info.bio,
            'scoreFacility': get_average_value(fac_info.evaluation_equipment),
            'scoreMeal': get_average_value(fac_info.evaluation_meal),
            'scoreSchedule': get_average_value(fac_info.evaluation_schedule),
            'scoreCost': get_average_value(fac_info.evaluation_cost),
            'scoreService': get_average_value(fac_info.evaluation_service),
            'overall': get_average_value(fac_info.overall),
            'oneLineE': one_line_e[:3]
        }, 200


@api.resource('/care_worker/<care_worker_id>')
class ShowParticularCareWorker(BaseResource):
    @swag_from(DAUGHTER_SHOW_CARE_WORKER_INFO_GET)
    def get(self, care_worker_id):
        care_worker = CareWorkerModel.objects(id=care_worker_id).first()

        if not care_worker:
            abort(400)

        def get_average_value(val):
            return round(val / care_worker.evaluation_count, 1) if care_worker.evaluation_count != 0 else 0

        one_line_e = [e for e in care_worker.one_line_evaluation]

        fac = FacilityModel.objects(facility_code=care_worker.facility_code).first()

        return {
            'imagePath': care_worker.image_path,
            'name': care_worker.name,
            'workplace': fac.name if fac else None,
            'patientInCharge': care_worker.patient_in_charge,
            'career': care_worker.career,
            'bio': care_worker.bio,
            'scoreDiligence': get_average_value(care_worker.evaluation_diligence),
            'scoreKindness': get_average_value(care_worker.evaluation_kindness),
            'overall': get_average_value(care_worker.overall),
            'oneLineE': one_line_e[:3]
        }, 200
