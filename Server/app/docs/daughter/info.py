DAUGHTER_SHOW_FACILITY_INFO_GET = {
    'tags': ['[Daughter] 순위'],
    'description': '특정 요양시설의 세부정보 조회',
    'parameters': [
        {
            'name': 'facility_code',
            'description': '상세정보를 조회하고 싶은 특정 병원의 코드(고유 식별자)',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '상세정보 조회 성공',
            'examples': {
                '': {
                    'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                    'name': '종현 요양병원',
                    'phoneNumber': '02-1234-5678',
                    'address': '서울특별시 강남구 이종현로 224',
                    'bio': '치매노인 전문 종현 요양병원 입니다^^ 믿고 맡겨주세요',
                    'scoreFacility': 4.7,
                    'scoreMeal': 3,
                    'scoreSchedule': 4.3,
                    'scoreCost': 4.8,
                    'scoreService': 4.9,
                    'overall': 3.5,
                    'oneLineE': ['친절해요', '마스코트가 귀여워요', '싸요']
                }
            }
        },
        '400': {
            'description': '존재하지 않는 요양시설'
        }
    }
}

DAUGHTER_SHOW_CARE_WORKER_INFO_GET = {
    'tags': ['[Daughter] 순위'],
    'description': '특정 요양보호사의 세부정보 조회',
    'parameters': [
        {
            'name': 'care_worker_id',
            'description': '상세정보를 조회하고 싶은 특정 보호사의 고유 id',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '상세정보 조회 성공',
            'examples': {
                '': {
                    'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                    'name': '이종',
                    'workplace': '종현 요양병원',
                    'patientInCharge': 6,
                    'career': 4,
                    'bio': '안녕하세요 믿음직한 보호사 이종현입니다.',
                    'scoreDiligence': 4.7,
                    'scoreKindness': 3,
                    'overall': 3.5,
                    'oneLineE': ['친절해요', '귀여워요', '용돈주세요']
                }
            }
        },
        '400': {
            'description': '존재하지 않는 요양보호사'
        }
    }
}
