from flask import Blueprint, request, abort
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import check_password_hash
from flasgger import swag_from

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel, DaughterModel
from app.models.facility import FacilityModel

from app.docs.daughter.rangking import DAUGHTER_RANKING_FACILITY_GET


api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/ranking'


@api.resource('/facility')
class RankingFacility(BaseResource):
    @swag_from(DAUGHTER_RANKING_FACILITY_GET)
    def get(self):
        """
        요양시설의 순위(overall 기준) API
        - 로그인이 되어 있지않다면 순위만 조회할 수 있다.
        - 로그인이 되어있다면 순위와 함께 자신이 이용하고 있는 시설의 정보도 조회하고 평가할 수 있다.
        - 순위에 표시되는 시설의 정보는 다음과 같다.
            - 시설 이름, 시설 주소, 평가 총점, 칭호(있다면 열거함), 시설 전경(사진)
        """
        def overlap_facility_data(facility_obj):
            return {
                'facility_code': facility_obj.facility_code,
                'name': facility_obj.name,
                'address': facility_obj.address,
                'overall': round(facility_obj.overall / facility_obj.evaluation_count, 1),
                'medals': [medal for medal in facility_obj.medals if medal is not None]
            }

        info = {
            'facilityRanking': [overlap_facility_data(facility)
                                for facility in FacilityModel.objects.order_by('-overall')]
        }

        if request.headers['Authorization']:
            info['myFacilities'] = \
                [overlap_facility_data(facility) for facility in
                 [FacilityModel.objects(facility_code=my_fac.facility_code).first() for my_fac in
                  [c for c in DaughterModel.objects(id=get_jwt_identity()).first().care_workers]]]

        return info, 200


@api.resource('/care_worker')
class RankingCareWorker(BaseResource):
    def get(self):
        pass

