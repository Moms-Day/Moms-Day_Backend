DAUGHTER_VIEW_ACCOUNT_INFO_GET = {
    'tags': ['[Daughter] 계정'],
    'description': '마이페이지',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '요청 성공',
            'examples': {
                '': {
                    'name': '이름',
                    'age': 22,
                    'patients': [
                        {
                            'name': '노인1',
                            'age': 77,
                            'gender': True
                        },
                        {
                            'name': '노읹2',
                            'age': 88,
                            'gender': False
                        }
                    ]
                }
            }
        }
    }
}

DAUGHTER_CHANGE_PASSWORD_PATCH = {
    'tags': ['[Daughter] 계정'],
    'description': '비밀번호 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'currentPw',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'newPw',
            'description': '바꿀 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '비밀번호 변경 성공',
        },
        '403': {
            'description': '현재 비밀번호 불일치'
        }
    }
}

DAUGHTER_WITHDRAW_DELETE = {
    'tags': ['[Daughter] 계정'],
    'description': '회원 탈퇴',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '탈퇴 성공',
        },
        '403': {
            'description': '현재 비밀번호 불일치'
        }
    }
}
