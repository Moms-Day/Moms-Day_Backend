from flask import Blueprint, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource

from app.models.facility import FacilityModel

from app.docs.daughter.info import DAUGHTER_SHOW_FACILITY_INFO_GET


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
            return round(val / fac_info.evaluation_count, 1)

        one_line_e = [e for e in fac_info.one_line_evaluation]

        return {
            'name': fac_info.name,
            'phone_number': fac_info.phone_number,
            'address': fac_info.address,
            'bio': fac_info.bio,
            'score_facility': get_average_value(fac_info.evaluation_facility),
            'score_meal': get_average_value(fac_info.evaluation_meal),
            'score_schedule': get_average_value(fac_info.evaluation_schedule),
            'score_cost': get_average_value(fac_info.evaluation_cost),
            'score_service': get_average_value(fac_info.evaluation_service),
            'overall': get_average_value(fac_info.overall),
            'one_line_e': one_line_e[:3]
        }, 200


@api.resource('/care_worker/<obj_id>')
class ShowParticularCareWorker(BaseResource):
    def get(self):
        pass
