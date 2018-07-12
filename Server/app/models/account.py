from datetime import datetime

from mongoengine import *


class AccountBase(Document):
    """
    CareWorker 계정과 Daughter 계정의 상위 collection
    """

    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    id = StringField(
        primary_key=True,
        max_length=20
    )

    pw = StringField(
        required=True
    )

    name = StringField(
        required=True,
        max_length=20
    )

    signup_time = DateTimeField(
        default=datetime.now
    )

    phone_number = StringField(
        required=True
    )

    certify_code = StringField(
        # required=True
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
        # required=True
    )

    # profile_image = ImageField(
    #
    # )

    bio = StringField(
        required=True,
        max_length=300
    )

    # 평가 정보
    evaluation_diligence = LongField()
    evaluation_kindness = LongField()
    overall = FloatField()
    one_line_evaluation = ListField(
        StringField(max_length=150)
    )

    evaluation_count = LongField()

    # patients = ListField(
    #     ReferenceField(document_type='PatientModel')
    # )


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

    care_workers = ListField(
        ReferenceField(document_type='CareWorkerModel')
    )


class CertifyCodesModel(Document):
    certify_code = StringField(required=True)


class FacilityCodesModel(Document):
    name = StringField(required=True)
    facility_code = StringField(required=True)
