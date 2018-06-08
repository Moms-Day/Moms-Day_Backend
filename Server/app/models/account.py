from datetime import datetime

from mongoengine import *


class BeforeCertifyModel(Document):
    meta = {
        'collection': 'before_certify'
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

    certify_code = StringField(
        required=True
    )


class CareWorkerModel(AccountBase):
    """
    CareWorker 의 계정 collection
    """
    meta = {
        'collection': 'care_worker_account'
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
    """
    Daughter 의 계정 collection
    """

    meta = {
        'collection': 'daughter_account'
    }

    age = IntField(
        required=True
    )
