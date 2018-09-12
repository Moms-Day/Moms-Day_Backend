import datetime

from flask import Blueprint, abort
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource, auth_required

from app.models.account import CareWorkerModel, DaughterModel
from app.models.patient import PatientModel
from app.models.patient import *

from app.docs.daughter.forms import DAUGHTER_VIEW_FORM_GET

api = Api(Blueprint(__name__, __name__))


@api.resource('/daughter/main')
class GetPatients(BaseResource):
    @auth_required
    def get(self):
        daughter = DaughterModel.objects(id=get_jwt_identity()).first()
        return [patient.id for patient in PatientModel.objects(daughter=daughter) if patient.care_worker], 200


@api.resource('/daughter/form/<p_id>')
class ViewForm(BaseResource):
    @swag_from(DAUGHTER_VIEW_FORM_GET)
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        def todays_report(p, date):
            meal = MealMenu.objects(patient=p, date=date).first()
            schedule = Schedule.objects(patient=p, date=date).first()
            photo = RepresentativePhoto.objects(patient=p, date=date).first()
            condition = PhysicalCondition.objects(patient=p, datetime=date).first()

            return {
                'date': str(date),
                'meal': {
                    'breakfast': str(meal.breakfast).split(' '),
                    'lunch': str(meal.lunch).split(' '),
                    'dinner': str(meal.dinner).split(' ')
                },
                'schedule': [{
                    'time': table.start + ' ~ ' + table.end,
                    'work': table.work
                } for table in ScheduleTimeTables.objects(schedule=schedule)],
                'condition': [{
                    k: v
                } for k, v in dict(condition.to_mongo()).items() if type(v) == bool and v is True],
                'photo': {
                    'photo_path': photo.image_path,
                    'comment': photo.comment
                }
            }

        daughter = DaughterModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id).first()
        current_date = datetime.datetime.utcnow().date()

        if not patient:
            abort(400)

        if patient.daughter.id != daughter.id:
            abort(403)

        return {
            'today': todays_report(patient, current_date),
            'yesterday': todays_report(patient, current_date - datetime.timedelta(days=1)),
            '2days_ago': todays_report(patient, current_date - datetime.timedelta(days=2))
        }
