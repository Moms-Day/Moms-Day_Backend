import datetime

from flask import Blueprint, abort
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource, auth_required

from app.models.facility import FacilityModel
from app.models.account import CareWorkerModel, DaughterModel
from app.models.patient import PatientModel
from app.models.patient import *

from app.docs.daughter.forms import DAUGHTER_VIEW_FORM_GET, DAUGHTER_GET_PATIENTS_ID_GET

api = Api(Blueprint(__name__, __name__))


@api.resource('/daughter/main')
class GetPatients(BaseResource):
    @swag_from(DAUGHTER_GET_PATIENTS_ID_GET)
    @auth_required(DaughterModel)
    def get(self):
        daughter = DaughterModel.objects(id=get_jwt_identity()).first()
        return [{
            'id': patient.id,
            'name': patient.name,
            'careId': patient.care_worker.id,
            'careName': patient.care_worker.name,
            'facilityCode': patient.care_worker.facility_code,
            'facilityName': FacilityModel.objects(facility_code=patient.care_worker.facility_code).first().name
        } for patient in PatientModel.objects(daughter=daughter) if patient.care_worker], 200


@api.resource('/daughter/form/<p_id>')
class ViewForm(BaseResource):
    @swag_from(DAUGHTER_VIEW_FORM_GET)
    @auth_required(DaughterModel)
    def get(self, p_id):
        def todays_report(p, date):
            meal = MealMenu.objects(patient=p, date=date).first()
            schedule = Schedule.objects(patient=p, date=date).first()
            photo = RepresentativePhoto.objects(patient=p, date=date).first()
            condition = PhysicalCondition.objects(patient=p, date=date).first()
            additional = AdditionalDescription.objects(patient=p, date=date).first()

            return {
                'date': str(date),
                'meal': {
                    'breakfast': str(meal.breakfast).split('\n'),
                    'lunch': str(meal.lunch).split('\n'),
                    'dinner': str(meal.dinner).split('\n'),
                    'snack': meal.snack
                } if meal else {},
                'schedule': [{
                    'time': table.start + ' ~ ' + table.end,
                    'work': table.work
                } for table in ScheduleTimeTables.objects(schedule=schedule)] if schedule else [],
                'condition': {k: v for k, v in
                              dict(condition.to_mongo()).items() if type(v) == bool and v is True} if condition else {},
                'photo': {
                    'photo_path': photo.image_path,
                    'comment': photo.comment
                } if photo else {},
                'additional': {
                    'description': additional.description
                } if additional else {}
            }

        daughter = DaughterModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id).first()
        current_date = datetime.datetime.utcnow().date()

        if not patient:
            abort(400)

        if patient.daughter.id != daughter.id:
            abort(403)

        return self.unicode_safe_json_dumps({
            'today': todays_report(patient, current_date),
            'yesterday': todays_report(patient, current_date - datetime.timedelta(days=1)),
            '2days_ago': todays_report(patient, current_date - datetime.timedelta(days=2))
        }, 200)
