DAUGHTER_SEARCH_FOR_CONNECTION_GET = {
    'tags': ['[Daughter] 연결'],
    'description': '연결 요청을 위한 요양시설 검색',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'facilityName',
            'description': '검색하고 싶은 요양시설(검색어)',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '검색 성공',
            'examples': {
                '검색어에 해당하는 데이터 있음': {
                    'data': [
                        {
                            'facilityCode': '000010',
                            'name': '서울요양병원',
                            'address': '서울시 서초구 서초대로',
                            'careWorkers': [
                                {
                                    'id': 'papered',
                                    'name': '이종현'
                                },
                                {
                                    'id': 'popue',
                                    'name': '김이박'
                                }
                            ]
                        },
                        {
                            'facilityCode': '000013',
                            'name': '인직요양원',
                            'address': '인천광역시 미추홀',
                            'careWorkers': [
                                {
                                    'id': 'dddd',
                                    'name': '카베요'
                                },
                                {
                                    'id': 'hhaa',
                                    'name': '카밀라'
                                }
                            ]
                        }
                    ]
                },
                '검색어에 해당하는 데이터 없음': {
                    'data': [

                    ]
                }
            }
        }
    }
}

DAUGHTER_REQUEST_CONNECTION_POST = {
    'tags': ['[Daughter] 연결'],
    'description': '특정 요양보호사에게 연결 요청',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'careId',
            'description': '연결 요청할 요양보호사의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'requesterId',
            'description': '요청하는 자녀의 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'requesterName',
            'description': '요청하는 자녀의 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'patientName',
            'description': '보호사에게 맡길 노부모의 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'patientAge',
            'description': '보호사에게 맡길 노부모의 나이',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'patientGender',
            'description': '보호사에게 맡길 노부모의 성별',
            'in': 'json',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '연결 요청 성공'
        }
    }
}
