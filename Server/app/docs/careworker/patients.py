CARE_VIEW_PATIENTS_LIST_GET = {
    'tags': ['[CareWorker] 연결'],
    'description': '보호사 본인에게 온 요청목록과 본인이 담당하고 있는 노인 목록 조회',
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
            'description': '요청 목록 및 담당 노인 목록 조회 성공',
            'examples': {
                'no data': {
                    'connectionRequests': [],
                    'inChargeList': []
                },

                '': {
                    'connectionRequests': [
                        {
                            'req_id': '234512351cc4',
                            'requester_id': 'qwer45',
                            'r_name': '정다은',
                            'p_name': '이종현',
                            'p_age': 68,
                            'p_gender': True,
                            'request_time': '2018-08-29 19:19:33.047928'
                        },
                        {
                            'req_id': 'cjej3if2i409rc',
                            'requester_id': 'qwer46',
                            'r_name': '이종현',
                            'p_name': '정다은',
                            'p_age': 67,
                            'p_gender': False,
                            'request_time': '2018-08-30 19:19:33.047928'
                        }
                    ],
                    'inChargeList': [
                        {
                            'id': 'aaaaaaaaaaaa1',
                            'name': '김우진',
                            'age': 83,
                            'gender': True,
                            'daughter': '김이박'
                        },
                        {
                            'id': 'bbbbbbbbbb2',
                            'name': '최정',
                            'age': 75,
                            'gender': False,
                            'daughter': '최정 아들'
                        }
                    ]
                }
            }
        }
    }
}

CARE_ACCEPT_OR_REJECT_REQUESTS_PATCH = {
    'tags': ['[CareWorker] 연결'],
    'description': '요청을 수락 또는 거절',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '본인에게 요청한 자녀의 아이디',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'reqId',
            'description': '요청 고유 아이디',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'accept',
            'description': '수락 => True, 거절 => False',
            'in': 'json',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '수락 or 거절 성공',
        },
        '400': {
            'description': '존재하지 않는 자녀 아이디 or 요청 아이디'
        }
    }
}

CARE_VIEW_PATIENT_MEMO_GET = {
    'tags': ['[CareWorker] 연결'],
    'description': '담당 노인의 메모 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'p_id',
            'description': '메모를 보고 싶은 노인의 id',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '메모 조회 성공',
        }
    }
}

CARE_MODIFY_PATIENT_MEMO_PATCH = {
    'tags': ['[CareWorker] 연결'],
    'description': '담당 노인의 메모 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'p_id',
            'description': '메모를 수정하고 싶은 노인의 id',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'memo',
            'description': '수정할 메모',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '메모 수정 성공',
        }
    }
}
