# import datetime
#
# from flask import Blueprint, request, Response, abort
# from flask_restful import Api
# from flasgger import swag_from
#
# from app.views import BaseResource, json_required, auth_required
#
# from app.models.account import CareWorkerModel
# from app.models.patient import *
#
# api = Api(Blueprint(__name__, __name__))
# api.prefix = '/care/update/form'
#
#
# @api.resource('/meal')
# class UpdateFormOfMeal(BaseResource):
#     # key 를 카멜 케이스로
#     @auth_required(CareWorkerModel)
#     @json_required({
#         'pId': str
#     })
#     def patch(self):
#         payload = dict(request.json)
#
#         return Response('', 201)
