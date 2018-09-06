import datetime
import base64
import os

from flask import Blueprint, request, Response, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel
from app.models.patient import *

from app.docs.careworker.update_form import *

api = Api(Blueprint(__name__, __name__))
api.prefix = '/care/update/form'


@api.resource('/meal')
class UpdateFormOfMeal(BaseResource):
    @swag_from(CARE_UPDATE_MEAL_FORM_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'breakfast': str,
        'lunch': str,
        'dinner': str,
        'snack': str,
        'pId': str
    })
    def patch(self):
        payload = request.json
        current_date = datetime.datetime.utcnow().date()
        patient = PatientModel.objects(id=payload['pId']).first()

        if not patient:
            abort(400)

        meal_form = MealMenu.objects(patient=patient, date=current_date).first()

        if not meal_form:
            abort(428)

        data = {
            'breakfast': payload['breakfast'],
            'lunch': payload['lunch'],
            'dinner': payload['dinner'],
            'snack': payload['snack'],
        }

        meal_form.update(**data)

        return Response('', 201)


@api.resource('/schedule')
class UpdateFormOfSchedule(BaseResource):
    @swag_from(CARE_UPDATE_SCHEDULE_FORM_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str
    })
    def patch(self):
        payload = request.json
        current_date = datetime.datetime.utcnow().date()
        patient = PatientModel.objects(id=payload['pId']).first()

        if not patient:
            abort(400)

        schedule_form = Schedule.objects(patient=patient, date=current_date).first()

        if not schedule_form:
            abort(428)

        time_tables = ScheduleTimeTables.objects(s=schedule_form)

        for table in time_tables:
            for d in payload['schedules']:
                table.update(start=d['start'], end=d['end'], work=d['work'])

        return Response('', 201)


@api.resource('/photo')
class UpdateFormOfPhoto(BaseResource):
    @swag_from(CARE_UPDATE_PHOTO_FORM_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str,
        'encodedImage': str,
        'comment': str
    })
    def patch(self):
        def convert_and_save(b64_string, path):
            with open(path, "wb+") as fh:
                fh.write(base64.b64decode(b64_string.encode()))

        payload = request.json
        patient = PatientModel.objects(id=payload['pId']).first()
        current_date = datetime.datetime.utcnow().date()
        image_path = "./static/imgs/repersentative_photo/" + str(patient.id) + str(current_date) + ".jpg"

        if not patient:
            abort(400)

        if os.path.isfile(image_path):
            os.remove(image_path)
        else:
            abort(400)

        photo_form = RepresentativePhoto.objects(patient=patient, date=current_date).first()

        if not photo_form:
            abort(428)

        convert_and_save(payload['encodedImage'], image_path)

        data = {
            'image_path': image_path,
            'comment': payload['comment'],
        }

        photo_form.update(**data)

        return Response('', 201)


@api.resource('/condition')
class UpdateFormOfCondition(BaseResource):
    @swag_from(CARE_UPDATE_CONDITION_FORM_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str
    })
    def patch(self):
        current_date = datetime.datetime.utcnow().date()
        payload = dict(request.json)
        p_id = payload.pop('pId')
        patient = PatientModel.objects(id=p_id).first()

        if not patient:
            abort(400)

        condition_form = PhysicalCondition.objects(patient=patient, date=current_date)

        if not condition_form:

        condition_form.update(**payload)

        return Response('', 201)
