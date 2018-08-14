from flask import Blueprint, request, Response, abort
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel, DaughterModel
from app.models.facility import FacilityModel

from app.docs.daughter.evaluate import *


api = Api(Blueprint(__name__, __name__))
api.prefix = '/daughter/evaluate'


@api.resource('/facility/<facility_code>')
class EvaluateMyFacility(BaseResource):
    @swag_from(DAUGHTER_EVALUATE_FACILITY_PATCH)
    @auth_required(DaughterModel)
    @json_required({
        'equipment': int,
        'meal': int,
        'schedule': int,
        'cost': int,
        'service': int,
        'overall': float
    })
    def patch(self, facility_code):
        target = FacilityModel.objects(facility_code=facility_code).first()

        if not target:
            abort(400)

        evaluation = {
            'evaluation_equipment': target.evaluation_equipment + request.json['equipment'],
            'evaluation_meal': target.evaluation_meal + request.json['meal'],
            'evaluation_schedule': target.evaluation_schedule + request.json['schedule'],
            'evaluation_cost': target.evaluation_cost + request.json['cost'],
            'evaluation_service': target.evaluation_service + request.json['service'],
            'overall': target.overall + request.json['overall'],
            'evaluation_count': 1 + target.evaluation_count
        }

        if request.json['lineE']:
            target.one_line_evaluation.append(request.json['lineE'])
            target.save()

        target.update(**evaluation)

        return Response('', 201)


@api.resource('/care_worker/<care_worker_id>')
class EvaluateMyCareWorker(BaseResource):
    @swag_from(DAUGHTER_EVALUATE_CARE_WORKER_PATCH)
    @auth_required(DaughterModel)
    @json_required({
        'diligence': int,
        'kindness': int,
        'overall': float
    })
    def patch(self, care_worker_id):
        target = CareWorkerModel.objects(id=care_worker_id).first()

        if not target:
            abort(400)

        evaluation = {
            'evaluation_diligence': target.evaluation_diligence + request.json['diligence'],
            'evaluation_kindness': target.evaluation_kindness + request.json['kindness'],
            'overall': target.overall + request.json['overall'],
            'evaluation_count': 1 + target.evaluation_count
        }

        if request.json['lineE']:
            target.one_line_evaluation.append(request.json['lineE'])
            target.save()

        target.update(**evaluation)

        return Response('', 201)
