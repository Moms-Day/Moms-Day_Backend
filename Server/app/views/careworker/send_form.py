import datetime
import base64

from flask import Blueprint, request, Response, abort, current_app
from flask_restful import Api
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel
from app.models.patient import *

from app.docs.careworker.send_form import *

api = Api(Blueprint(__name__, __name__))
api.prefix = '/care/send/form'


@api.resource('/meal')
class SendFormOfMeal(BaseResource):
    @swag_from(CARE_SEND_MEAL_FORM_POST)
    @auth_required(CareWorkerModel)
    @json_required({
        'breakfast': str,
        'lunch': str,
        'dinner': str,
        'snack': str,
        'pId': str
    })
    def post(self):
        payload = request.json
        patient = PatientModel.objects(id=payload['pId']).first()

        if not patient:
            abort(400)

        data = {
            'date': datetime.datetime.utcnow().date(),
            'breakfast': payload['breakfast'],
            'lunch': payload['lunch'],
            'dinner': payload['dinner'],
            'snack': payload['snack'],
            'patient': patient
        }

        MealMenu(**data).save()

        return Response('', 201)


@api.resource('/schedule')
class SendFormOfSchedule(BaseResource):
    @swag_from(CARE_SEND_SCHEDULE_FORM_POST)
    @auth_required(CareWorkerModel)
    def post(self):
        payload = request.json
        patient = PatientModel.objects(id=payload['pId']).first()

        if not patient:
            abort(400)

        s = Schedule(date=datetime.datetime.utcnow().date(),
                     patient=patient).save()

        for d in payload['schedules']:
            ScheduleTimeTables(schedule=s, start=d['start'], end=d['end'], work=d['work']).save()

        return Response('', 201)


@api.resource('/photo')
class SendFormOfPhoto(BaseResource):
    @swag_from(CARE_SEND_PHOTO_FORM_POST)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str,
        'encodedImage': str,
        'comment': str
    })
    def post(self):
        def convert_and_save(b64_string, path):
            with open(path, "wb+") as fh:
                fh.write(base64.b64decode(b64_string.encode()))

        payload = request.json
        patient = PatientModel.objects(id=payload['pId']).first()
        current_date = datetime.datetime.utcnow().date()
        image_path = "./static/imgs/repersentative_photo/" + str(patient.id) + str(current_date) + ".jpg"

        if not patient:
            abort(400)

        convert_and_save(payload['encodedImage'], image_path)

        data = {
            'date': current_date,
            'image_path': str(current_app.config['PUBLIC_HOST']) + ":" + str(current_app.config['PORT']) + image_path[8:],
            'comment': payload['comment'],
            'patient': patient
        }

        RepresentativePhoto(**data).save()

        return Response('', 201)


@api.resource('/condition')
class SendFormOfCondition(BaseResource):
    @swag_from(CARE_SEND_CONDITION_FORM_POST)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str
    })
    def post(self):
        current_date = datetime.datetime.utcnow().date()
        payload = dict(request.json)
        p_id = payload.pop('pId')
        patient = PatientModel.objects(id=p_id).first()

        if not patient:
            abort(400)

        payload.update({'patient': patient, 'date': current_date})
        print(payload)
        PhysicalCondition(**payload).save()

        return Response('', 201)


@api.resource('/additional')
class SendFormOfAdditional(BaseResource):
    @swag_from(CARE_SEND_ADDITIONAL_FORM_POST)
    @auth_required(CareWorkerModel)
    @json_required({
        'pId': str,
        'description': str
    })
    def post(self):
        payload = request.json
        patient = PatientModel.objects(id=payload['pId']).first()

        if not patient:
            abort(400)

        AdditionalDescription(
            date=datetime.datetime.utcnow().date(),
            description=payload['description'],
            patient=patient
        ).save()

        return Response('', 201)


@api.resource('/meal/<p_id>')
class ViewPostedMealForm(BaseResource):
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        current_date = datetime.datetime.utcnow().date()
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id, care_worker=care).first()

        if not patient:
            abort(400)

        meal = MealMenu.objects(patient=patient, date=current_date).first()

        return self.unicode_safe_json_dumps({
            'breakfast': str(meal.breakfast).split('\n'),
            'lunch': str(meal.lunch).split('\n'),
            'dinner': str(meal.dinner).split('\n'),
            'snack': meal.snack
        }, 200) if meal else {}


@api.resource('/schedule/<p_id>')
class ViewPostedScheduleForm(BaseResource):
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        current_date = datetime.datetime.utcnow().date()
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id, care_worker=care).first()

        if not patient:
            abort(400)

        schedule = Schedule.objects(patient=patient, date=current_date).first()

        return self.unicode_safe_json_dumps([{
            'time': table.start + ' ~ ' + table.end,
            'work': table.work
        } for table in ScheduleTimeTables.objects(schedule=schedule)], 200) if schedule else []


@api.resource('/photo/<p_id>')
class ViewPostedPhotoForm(BaseResource):
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        current_date = datetime.datetime.utcnow().date()
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id, care_worker=care).first()

        if not patient:
            abort(400)

        photo = RepresentativePhoto.objects(patient=patient, date=current_date).first()

        return {
            'photo_path': photo.image_path,
            'comment': photo.comment
        } if photo else {}


@api.resource('/condition/<p_id>')
class ViewPostedConditionForm(BaseResource):
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        current_date = datetime.datetime.utcnow().date()
        care = CareWorkerModel.objects(id=get_jwt_identity()).first()
        patient = PatientModel.objects(id=p_id, care_worker=care).first()

        if not patient:
            abort(400)

        condition = PhysicalCondition.objects(patient=patient, date=current_date).first()

        return [{
            k: v
        } for k, v in dict(condition.to_mongo()).items() if type(v) == bool and v is True] if condition else []
