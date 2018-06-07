from datetime import datetime

from mongoengine import *


class SignupWaitingModel(Document):
    meta = {
        'collection': 'signup_waiting_model'
    }

    phone_number = StringField(
        required=True
    )

    certify_number = StringField(
        primary_key=True
    )

    # CareWork : True, Daughter : False
    app_type = BooleanField(

    )


class AccountBase(Document):
    """
    CareWorker 계정과 Daughter 계정의 상위 collection
    """

    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    id = StringField(
        primary_key=True
    )

    pw = StringField(
        required=True
    )

    name = StringField(
        required=True
    )

    signup_time = DateTimeField(
        default=datetime.now()
    )

    phone_number = StringField(
        required=True
    )

    certify_number = StringField(
        required=True
    )


class CareWorkerModel(AccountBase):
    meta = {
        'collection': 'care_worker_model'
    }

    career = IntField(
        required=True
    )

    patient_in_charge = IntField(
        required=True
    )

    facility_code = StringField(
        required=True
    )

    bio = StringField(
        required=True
    )


class DaughterModel(AccountBase):
    pass
