from app.docs import SAMPLE_FACILITY_CODE

DAUGHTER_RANKING_FACILITY_GET = {
    'tags': ['[Daughter] 순위'],
    'description': '요양 시설 순위 조회(no token => Only ranking, have token => ranking & own facilities)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': '순위 조회 성공',
            'examples': {
                'no token': {
                        'facilityRanking': [
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[0],
                                'name': '무슨무슨 요양병원',
                                'address': '어디어디 어디 어디어디 옆',
                                'overall': 4.5,
                                'medals': ['가성비 갑', '안전 점검 우수']
                            },
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[1],
                                'name': '어쩌구저쩌구 요양병원',
                                'address': '왼오왼오 옆옆 어디어디 어디',
                                'overall': 3,
                                'medals': []
                            },
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[2],
                                'name': '블라블라 노인 요양원',
                                'address': '바로 거기',
                                'overall': 2.5,
                                'medals': ['가성비 갑', '보호사 친절도 짱']
                            }
                        ]
                },
                'have token': {
                        'facilityRanking': [
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[0],
                                'name': '무슨무슨 요양병원',
                                'address': '어디어디 어디 어디어디 옆',
                                'overall': 4.5,
                                'medals': ['가성비 갑', '안전 점검 우수']
                            },
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[1],
                                'name': '어쩌구저쩌구 요양병원',
                                'address': '왼오왼오 옆옆 어디어디 어디',
                                'overall': 3,
                                'medals': []
                            },
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[2],
                                'name': '블라블라 노인 요양원',
                                'address': '바로 거기',
                                'overall': 2.5,
                                'medals': ['가성비 갑', '보호사 친절도 짱']
                            }
                        ],
                        'myFacilities': [
                            {
                                'facility_code': SAMPLE_FACILITY_CODE[3],
                                'name': '여기 엄마 모신곳 병원',
                                'address': '우리집에서 차타고 20분 거리에 있는 이마트 옆',
                                'overall': 1.5,
                                'medals': []
                            }
                        ]
                }
            }
        }
    }
}


