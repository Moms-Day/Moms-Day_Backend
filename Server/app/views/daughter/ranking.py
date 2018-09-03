from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_optional
from flasgger import swag_from

from app.views import BaseResource

from app.models.account import CareWorkerModel, DaughterModel
from app.models.facility import FacilityModel
from app.models.patient import PatientModel

from app.docs.daughter.ranking import DAUGHTER_RANKING_FACILITY_GET, DAUGHTER_RANKING_CARE_WORKER_GET


api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/ranking'


@api.resource('/facility')
class RankingFacility(BaseResource):
    @jwt_optional
    @swag_from(DAUGHTER_RANKING_FACILITY_GET)
    def get(self):
        """
        요양시설의 순위(overall 기준) API
        - 로그인이 되어 있지않다면 순위만 조회할 수 있다.
        - 로그인이 되어있다면 순위와 함께 자신이 이용하고 있는 시설의 정보도 조회할 수 있다.
        - 순위에 표시되는 시설의 정보는 다음과 같다.
            - 시설 이름, 시설 주소, 평가 총점, 칭호(있다면 열거함), 시설 전경(사진)
        """
        def overlap_facility_data(facility_obj):
            return {
                'facilityCode': facility_obj.facility_code,
                'imagePath': facility_obj.image_path,
                'name': facility_obj.name,
                'address': facility_obj.address,
                'overall': round(facility_obj.overall / facility_obj.evaluation_count, 1)
                if facility_obj.evaluation_count != 0 else None,
                'medals': list(facility_obj.medals) if facility_obj.medals is not None else []
            } if facility_obj else {}

        # 전체 병원의 순위(overall 기준)
        info = {
            'facilityRanking': [overlap_facility_data(facility)
                                for facility in FacilityModel.objects.order_by('-overall')]
        }

        # 인증된 사용자라면 사용자 본인이 이용하고 있는 시설의 정보 추가
        if 'Authorization' in request.headers.keys():
            print(request.headers['Authorization'])

            patients = PatientModel.objects(DaughterModel.objects(id=get_jwt_identity()).first())
            cares = [patient.care_worker for patient in patients]
            facs = [FacilityModel.objects(facility_code=care.facility_code)for care in cares]

            info['myFacilities'] = [overlap_facility_data(fac) for fac in facs]

            # info['myFacilities'] = \
            #     [overlap_facility_data(facility) for facility in
            #      [FacilityModel.objects(facility_code=my_fac.facility_code).first() for my_fac in
            #       [c for c in DaughterModel.objects(id=get_jwt_identity()).first().care_workers]]]

        return info, 200


@api.resource('/care_worker')
class RankingCareWorker(BaseResource):
    @jwt_optional
    @swag_from(DAUGHTER_RANKING_CARE_WORKER_GET)
    def get(self):
        """
        요양 보호사의 순위(overall 기준) API
        - 로그인이 되어 있지않다면 순위만 조회할 수 있다.
        - 로그인이 되어있다면 순위와 함께 자신의 노인을 담당하고 있는 요양보호사의 정보도 조회할 수 있다.
        - 순위에 표시되는 시설의 정보는 다음과 같다.
            - 이름, 소속(요양시설), 담당 노인 수, 경력, 총점
        """
        def overlap_care_worker_data(worker_obj):
            return {
                'careWorkerId': worker_obj.id,
                'imagePath': worker_obj.image_path,
                'name': worker_obj.name,
                'workplace': FacilityModel.objects(facility_code=worker_obj.facility_code).first().name,
                'patientInCharge': worker_obj.patient_in_charge,
                'career': worker_obj.career,
                'overall': round(worker_obj.overall / worker_obj.evaluation_count, 1)
                if worker_obj.evaluation_count != 0 else None
            } if worker_obj else {}

        info = {
            'careWorkerRanking': [overlap_care_worker_data(care_worker)
                                  for care_worker in CareWorkerModel.objects.order_by('-overall')]
        }

        if 'Authorization' in request.headers.keys():
            info['myCareWorkers'] = [overlap_care_worker_data(care_worker)
                                     for care_worker
                                     in DaughterModel.objects(id=get_jwt_identity()).first().care_workers]

        return info, 200

#
# @api.resource('/plus')
# class Plus(BaseResource):
#     """
#     test api
#     """
#     def post(self):
#         FacilityModel(
#             facility_code=request.json['facilityCode'],
#             name=request.json['name'],
#             phone_number=request.json['phoneNumber'],
#             address=request.json['address'],
#             bio=request.json['bio'],
#             overall=request.json['overall'],
#             evaluation_count=request.json['evaluationCount'],
#             medals=request.json['medals']
#         ).save()
#
#         return '', 201
