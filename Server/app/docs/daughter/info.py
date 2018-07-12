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
                    'name': '종현 요양병원',
                    'phone_number': '02-1234-5678',
                    'address': '서울특별시 강남구 이종현로 224',
                    'bio': '치매노인 전문 종현 요양병원 입니다^^ 믿고 맡겨주세요',
                    'score_facility': 4.7,
                    'score_meal': 3,
                    'score_schedule': 4.3,
                    'score_cost': 4.8,
                    'score_service': 4.9,
                    'overall': 3.5,
                    'one_line_e': ['친절해요', '마스코트가 귀여워요', '싸요']
                }
            }
        },
        '400': {
            'description': '존재하지 않는 요양시설'
        }
    }
}
