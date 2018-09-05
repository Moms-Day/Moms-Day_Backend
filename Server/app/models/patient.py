import datetime

from mongoengine import *


class PatientModel(Document):
    id = StringField(
        required=True,
        primary_key=True
    )

    name = StringField(
        max_length=20, required=True
    )

    age = IntField(
        required=True
    )

    # male => True , female => False
    gender = BooleanField(
        required=True
    )

    memo = StringField(
        max_length=500
    )

    daughter = ReferenceField(
        document_type='DaughterModel'
    )

    care_worker = ReferenceField(
        document_type='CareWorkerModel'
    )


class MealMenu(Document):
    """
    오늘의 식단(조식, 중식, 석식) 및 추가 간식
    """

    date = DateTimeField(
        required=True,
        default=datetime.datetime.utcnow().date()
    )

    breakfast = StringField(
        required=True,
        default=""
    )

    lunch = StringField(
        required=True,
        default=""
    )

    dinner = StringField(
        required=True,
        default=""
    )

    snack = StringField(max_length=30, default="")

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class Schedule(Document):
    """
    하루 일정표
    """
    date = DateTimeField(
        required=True,
        default=datetime.datetime.utcnow().date()
    )

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class ScheduleTimeTables(Document):
    schedule = ReferenceField(
        document_type="Schedule",
        reverse_delete_rule=CASCADE
    )

    start = StringField(
        required=True,
        default=""
    )

    end = StringField(
        required=True,
        default=""
    )

    work = StringField(
        required=True,
        max_length=100,
        default=""
    )


class PhysicalCondition(Document):
    """
    하루 건강 상태
    """
    date = DateTimeField(
        required=True
    )

    activity_reduction = BooleanField(default=False) # 활동량 감소
    low_temperature = BooleanField(default=False) # 저체온
    high_fever = BooleanField(default=False) # 고열
    blood_pressure_increase = BooleanField(default=False) # 고혈압
    blood_pressure_reduction = BooleanField(default=False) # 저혈압
    lack_of_sleep = BooleanField(default=False) # 수면부족
    lose_Appetite = BooleanField(default=False) # 식욕 감퇴
    binge_eating = BooleanField(default=False) # 폭식
    diarrhea = BooleanField(default=False) # 설사
    constipation = BooleanField(default=False) # 변비
    vomiting = BooleanField(default=False) # 구토
    urination_inconvenient = BooleanField(default=False) # 배뇨활동 불편
    human_power_reduction = BooleanField(default=False) # 인지력 감퇴
    poverty_of_blood = BooleanField(default=False) # 빈혈
    cough = BooleanField(default=False) # 기침

    comment = StringField(required=True, max_length=300, default="특이사항 없음")

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class RepresentativePhoto(Document):
    """
    하루를 대표하는 사진
    """
    date = DateTimeField(
        required=True,
        default=datetime.datetime.utcnow().date()
    )

    image_path = StringField(

    )

    comment = StringField(max_length=200, default="")

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )
