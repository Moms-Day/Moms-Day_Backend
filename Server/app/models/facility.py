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

    image_path = StringField(

    )

    evaluation_equipment = LongField(default=0)
    evaluation_meal = LongField(default=0)
    evaluation_schedule = LongField(default=0)
    evaluation_cost = LongField(default=0)
    evaluation_service = LongField(default=0)
    overall = FloatField(default=0.0)
    one_line_evaluation = ListField(
        StringField(max_length=150)
    )

    evaluation_count = LongField(default=0)

    # 칭호는 백그라운드에서 시간마다 칭호조건을 체크하면서 부여
    medals = ListField(
        StringField()
    )
