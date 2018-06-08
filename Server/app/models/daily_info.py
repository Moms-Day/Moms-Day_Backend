from mongoengine import *


class Patient(Document):
    name = StringField(
        max_length=20
    )

    age = IntField(

    )

    memo = StringField(
        max_length=500
    )

    daughter = ReferenceField(
        document_type='DaughterModel'
    )

    care_workers = ListField(
        ReferenceField(
            document_type='CareWorkerModel'
        )
    )


class MealMenu(Document):
    """
    오늘의 식단(조식, 중식, 석식) 및 추가 간식
    """
    breakfast = ListField(StringField(

    ))

    lunch = ListField(StringField(

    ))

    dinner = ListField(StringField(

    ))

    snack = StringField(max_length=30)

    patient = ReferenceField(
        document_type='Patient'
    )


class Schedule(Document):
    """
    하루 일정표
    """
    time_column = ListField(
        DateTimeField()
    )

    work = ListField(
        StringField(max_length=100)
    )

    patient = ReferenceField(
        document_type='Patient'
    )


class PhysicalCondition(Document):
    """
    하루 건강 상태
    """
    activity_reduction = BooleanField(default=False, required=True)
    low_temperature = BooleanField(default=False, required=True)
    high_fever = BooleanField(default=False, required=True)
    blood_pressure_increase = BooleanField(default=False, required=True)
    blood_pressure_reduction = BooleanField(default=False, required=True)
    lack_of_sleep = BooleanField(default=False, required=True)
    lose_Appetite = BooleanField(default=False, required=True)
    binge_eating = BooleanField(default=False, required=True)
    diarrhea = BooleanField(default=False, required=True)
    constipation = BooleanField(default=False, required=True)
    vomiting = BooleanField(default=False, required=True)
    urination_inconvenient = BooleanField(default=False, required=True)
    human_power_reduction = BooleanField(default=False, required=True)
    poverty_of_blood = BooleanField(default=False, required=True)
    cough = BooleanField(default=False, required=True)
    bool_of_cough = BooleanField(default=False, required=True)

    comment = StringField(max_length=300)

    patient = ReferenceField(
        document_type='Patient'
    )


class RepresentativePhoto(Document):
    """
    하루를 대표하는 사진
    """
    photo = ImageField()

    comment = StringField(max_length=200)

    patient = ReferenceField(
        document_type='Patient'
    )
