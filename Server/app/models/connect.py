from datetime import datetime

from mongoengine import *


class RequestModel(Document):
    req_id = StringField(required=True, primary_key=True)

    # 요청한 대상(보호사)
    care_worker = ReferenceField(required=True, document_type='CareWorkerModel')

    requester_id = StringField(required=True)
    requester_name = StringField(required=True)

    patient_name = StringField(required=True)
    patient_age = IntField(required=True)
    # male => True , female => False
    patient_gender = BooleanField(
        required=True
    )

    request_time = DateTimeField(default=datetime.now)
