CARE_UPDATE_MEAL_FORM_PATCH = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '식사 관련 폼을 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pId',
            'description': '폼을 작성할 노인의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'breakfast',
            'description': '아침식사(메뉴는 띄어쓰기로 구분할것)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'lunch',
            'description': '점심식사(메뉴는 띄어쓰기로 구분할것)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'dinner',
            'description': '저녁식사(메뉴는 띄어쓰기로 구분할것)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'snack',
            'description': '간식',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '폼 수정 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        },
        '428': {
            'description': '작성되어있지 않은 폼(수정불가)'
        }
    }
}

CARE_UPDATE_SCHEDULE_FORM_PATCH = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '일정 관련 폼을 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pId',
            'description': '폼을 작성할 노인의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'schedules',
            'description': 'json 을 담은 배열',
            'in': 'json',
            'type': 'array',
            'required': True
        },
        {
            'name': 'start',
            'description': '일정 시작 시각(ex: 21:02)',
            'in': 'json-array',
            'type': 'str',
            'required': True
        },
        {
            'name': 'end',
            'description': '일정 종료 시각(ex: 21:02)',
            'in': 'json-array',
            'type': 'str',
            'required': True
        },
        {
            'name': 'work',
            'description': '한 일',
            'in': 'json-array',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '폼 수정 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        },
        '428': {
            'description': '작성되어있지 않은 폼(수정불가)'
        }
    }
}

CARE_UPDATE_PHOTO_FORM_PATCH = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '하루를 대표하는 사진에 관한 폼 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pId',
            'description': '폼을 작성할 노인의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'encodedImage',
            'description': '넣을 이미지를 base64로 인코딩해서 주세요',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'comment',
            'description': '사진 설명',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '폼 작성 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        },
        '428': {
            'description': '작성되어있지 않은 폼(수정불가)'
        }
    }
}

CARE_UPDATE_CONDITION_FORM_PATCH = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '오늘 노인의 건강상태 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pId',
            'description': '폼을 작성할 노인의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': '증상(종류가 많아서 description 에 첨부함)',
            'description': ' activity_reduction(활동량 감소), '
                           'low_temperature(저체온), high_fever(고열), blood_pressure_increase(고혈압), '
                           'blood_pressure_reduction(저혈압), lack_of_sleep(수면부족), lose_Appetite(식욕 감퇴), '
                           'binge_eating(폭식), diarrhea(설사), constipation(변비), vomiting(구토), '
                           'urination_inconvenient(배뇨활동 불편), human_power_reduction(인지력 감퇴), '
                           'poverty_of_blood(빈혈), cough(기침)',
            'in': 'json',
            'type': 'bool',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '폼 작성 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        },
        '428': {
            'description': '작성되어있지 않은 폼(수정불가)'
        }
    }
}

