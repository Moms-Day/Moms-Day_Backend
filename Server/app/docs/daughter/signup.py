DAUGHTER_SIGNUP_POST = {
    'tags': ['[Daughter] 계정'],
    'description': '자녀 회원 가입 (아직 SMS 인증이 구현되지 않음)',
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
            'name': 'name',
            'description': '자녀(사용자) 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'age',
            'description': '자녀(사용자) 나이',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'p_name',
            'description': '노부모 이름',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'p_age',
            'description': '노부모 나이',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'p_gender',
            'description': '노부모 성별',
            'in': 'json',
            'type': 'bool',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 및 환자(노인) 등록 성공'
        },
        '409': {
            'description': 'id 중복'
        }
    }
}
