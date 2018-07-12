DAUGHTER_EVALUATE_FACILITY_POST = {
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
            'name': 'evaluation_equipment',
            'description': '시설에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'evaluation_meal',
            'description': '식사에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'evaluation_schedule',
            'description': '일정에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'evaluation_cost',
            'description': '가격에 대한 평가',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'evaluation_service',
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
