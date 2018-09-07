CARE_MY_PAGE_GET = {
    'tags': ['[CareWorker] 계정'],
    'description': '마이페이지(프로필 사진과 이름)',
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
                    'profileImage': '이미지 경로임 글라이드에 쓰셈',
                    'name': '이름이름'
                }
            }
        }
    }
}

CARE_MODIFY_PROFILE_IMAGE_PATCH = {
    'tags': ['[CareWorker] 계정'],
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
            'name': 'encodedImage',
            'description': '변경할 이미지(base64 로 인코딩)',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '프로필 사진 변경 성공',
        }
    }
}

CARE_MODIFY_ACCOUNT_INFO_GET = {
    'tags': ['[CareWorker] 계정'],
    'description': '계정 정보 조회',
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
            'description': '조회 성공',
            'examples': {
                '': {
                    'name': '이름임',
                    'career': 3,
                    'patients': ['이종혀임', ' 이종종현임', 'tiara'],
                    'facility_code': '000010',
                    'bio': 'hello'
                }
            }
        }
    }
}

CARE_MODIFY_ACCOUNT_INFO_PATCH = {
    'tags': ['[CareWorker] 계정'],
    'description': '계정 정보 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '수정할 이름',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'career',
            'description': '수정할 경력',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'facilityCode',
            'description': '수정할 병원 코드',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'bio',
            'description': '수정할 자기소개',
            'in': 'json',
            'type': 'str',
            'required': False
        },
    ],
    'responses': {
        '201': {
            'description': '정보 수정 성공'
        }
    }
}

CARE_CHANGE_PASSWORD_PATCH = {
    'tags': ['[CareWorker] 계정'],
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
            'description': '비밀번호 변경 성공'
        },
        '401': {
            'description': '현재 비밀번호가 틀림'
        }
    }
}
