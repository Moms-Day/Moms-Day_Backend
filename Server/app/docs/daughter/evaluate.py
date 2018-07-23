DAUGHTER_EVALUATE_FACILITY_PATCH = {
    'tags': ['[Daughter] 순위'],
    'description': '자신이 이용하는 요양시설 평가',
    'parameters': [
        {
            'name': 'facility_code',
            'description': '평가하고 싶은 특정 병원의 코드(고유 식별자)',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'equipment',
            'description': '시설에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'meal',
            'description': '식사에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'schedule',
            'description': '일정에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'cost',
            'description': '가격에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'service',
            'description': '서비스에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'overall',
            'description': '총점',
            'in': 'json',
            'type': 'float',
            'required': True
        },
        {
            'name': 'lineE',
            'description': '한줄 평가',
            'in': 'json',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '평가 완료'
        },
        '400': {
            'description': '존재하지 않는 요양시설'
        }
    }
}

DAUGHTER_EVALUATE_CARE_WORKER_PATCH = {
    'tags': ['[Daughter] 순위'],
    'description': '컨택한 요양보호사 평가',
    'parameters': [
        {
            'name': 'care_worker_id',
            'description': '평가하고 싶은 특정 요양 보호사의 고유 id',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'diligence',
            'description': '성실도 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'kindness',
            'description': '친절도 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'overall',
            'description': '총점',
            'in': 'json',
            'type': 'float',
            'required': True
        },
        {
            'name': 'lineE',
            'description': '한줄 평가',
            'in': 'json',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '평가 완료'
        },
        '400': {
            'description': '존재하지 않는 요양보호사'
        }
    }
}
