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
        required=True
    )

    breakfast = ListField(StringField(
        required=True
    ))

    lunch = ListField(StringField(
        required=True
    ))

    dinner = ListField(StringField(
        required=True
    ))

    snack = StringField(max_length=30)

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class Schedule(Document):
    """
    하루 일정표
    """
    date = DateTimeField(
        required=True
    )

    time_column = ListField(
        DateTimeField(required=True)
    )

    work = ListField(
        StringField(max_length=100, required=True)
    )

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class PhysicalCondition(Document):
    """
    하루 건강 상태
    """
    date = DateTimeField(
        required=True
    )

    activity_reduction = BooleanField(default=False)
    low_temperature = BooleanField(default=False)
    high_fever = BooleanField(default=False)
    blood_pressure_increase = BooleanField(default=False)
    blood_pressure_reduction = BooleanField(default=False)
    lack_of_sleep = BooleanField(default=False)
    lose_Appetite = BooleanField(default=False)
    binge_eating = BooleanField(default=False)
    diarrhea = BooleanField(default=False)
    constipation = BooleanField(default=False)
    vomiting = BooleanField(default=False)
    urination_inconvenient = BooleanField(default=False)
    human_power_reduction = BooleanField(default=False)
    poverty_of_blood = BooleanField(default=False)
    cough = BooleanField(default=False)
    bool_of_cough = BooleanField(default=False)

    comment = StringField(max_length=300)

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )


class RepresentativePhoto(Document):
    """
    하루를 대표하는 사진
    """
    date = DateTimeField(

    )

    # photo = ImageField()

    comment = StringField(max_length=200)

    patient = ReferenceField(
        document_type='PatientModel',
        reverse_delete_rule=CASCADE
    )
