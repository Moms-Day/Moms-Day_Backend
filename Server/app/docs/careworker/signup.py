CARE_SIGNUP_POST = {
    'tags': ['[CareWorker] 계정'],
    'description': '요양보호사 회원 가입 (아직 SMS 인증이 구현되지 않음)',
    'parameters': [
        {
            'name': 'id',
            'description': 'id (20자 이내)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': 'password',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '요양보호사 이름 (20자 이내)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'career',
            'description': '요양보호사 경력(년)',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'patientInCharge',
            'description': '담당하고 있는 환자 수',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'phoneNumber',
            'description': '전화번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'certifyCode',
            'description': 'SMS 인증으로 받은 인증번호',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'facilityCode',
            'description': '소속 병원(요양시설) 코드',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'bio',
            'description': '자기소개 (300자 이내)',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '409': {
            'description': 'id 중복'
        }
    }
}
