from mongoengine import *


class FacilityModel(Document):
    facility_code = StringField(
        required=True,
        primary_key=True
    )

    name = StringField(
        required=True
    )

    phone_number = StringField(
        required=True
    )

    address = StringField(
        required=True
    )

    bio = StringField(
        max_length=100,
        required=True
    )

    evaluation_equipment = LongField()
    evaluation_meal = LongField()
    evaluation_schedule = LongField()
    evaluation_cost = LongField()
    evaluation_service = LongField()
    overall = FloatField()
    one_line_evaluation = ListField(
        StringField(max_length=150)
    )

    evaluation_count = LongField(default=0)

    # 칭호는 백그라운드에서 시간마다 칭호조건을 체크하면서 부여
    medals = ListField(
        StringField()
    )
