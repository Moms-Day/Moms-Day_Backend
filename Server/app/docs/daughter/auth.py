from app.docs import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN

DAUGHTER_AUTH_POST = {
    'tags': ['[Daughter] 계정'],
    'description': '자녀 로그인',
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
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': 'id 중복이나 잘못된 패스워드에 의해 로그인 실패'
        }
    }
}
