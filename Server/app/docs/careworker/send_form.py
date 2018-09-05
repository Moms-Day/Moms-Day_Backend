CARE_SEND_MEAL_FORM_POST = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '식사 관련 폼을 작성',
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
            'description': '폼 작성 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        }
    }
}

CARE_SEND_SCHEDULE_FORM_POST = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '일정 관련 폼을 작성',
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
            'description': '폼 작성 성공',
        },
        '400': {
            'description': '존재하지 않는 노인 id'
        }
    }
}

CARE_SEND_PHOTO_FORM_POST = {
    'tags': ['[CareWorker] 폼 작성'],
    'description': '하루를 대표하는 사진에 관한 폼 작성',
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
        }
    }
}
