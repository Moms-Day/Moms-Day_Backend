DAUGHTER_GET_PATIENTS_ID_GET = {
    'tags': ['[Daughter] 폼'],
    'description': '요양보호사와 연결된 자신의 노인 id 받아오기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': '폼 조회 성공',
            'examples': {
                '': ['id1', 'id2', 'id3']
            }
        }
    }
}


DAUGHTER_VIEW_FORM_GET = {
    'tags': ['[Daughter] 폼'],
    'description': '',
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
            'description': '폼을 조회할 노인의 id',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '폼 조회 성공',
            'examples': {
                '': {
                    'today': {
                        'date': '2018-09-09',
                        'meal': {
                            'breakfast': ['시리얼', '빵', '우유'],
                            'lunch': ['국수', '김치', '뭐시기', '오리'],
                            'dinner': ['고기', '깍두기', '음료수', '별로인거'],
                            'snack': '간식 먹지마'
                        },
                        'schedule': [{
                                        'time': '09:00 ~ 10:00',
                                        'work': '개발'
                                    },
                                    {
                                        'time': '11:00 ~ 12:00',
                                        'work': '잠'
                                    }],
                        'condition': [
                            {
                                'low_temperature': True
                            },
                            {
                                'lose_Appetite': True
                            },
                            {
                                'human_power_reduction': True
                            }
                        ],
                        'photo': {
                            'photo_path': '서버 어딘가',
                            'comment': '오늘 밥먹음'
                        },
                        'additional': {
                            'description': '추가사항임'
                        }
                    },
                    'yesterday': {
                        'date': '2018-09-08',
                        'meal': {
                            'breakfast': ['시리얼', '빵', '우유'],
                            'lunch': ['국수', '김치', '뭐시기', '오리'],
                            'dinner': ['고기', '깍두기', '음료수', '별로인거'],
                            'snack': '간식 먹지마'
                        },
                        'schedule': [{
                            'time': '09:00 ~ 10:00',
                            'work': '개발'
                        },
                            {
                                'time': '11:00 ~ 12:00',
                                'work': '잠'
                            }],
                        'condition': [
                            {
                                'low_temperature': True
                            },
                            {
                                'lose_Appetite': True
                            },
                            {
                                'human_power_reduction': True
                            }
                        ],
                        'photo': {
                            'photo_path': '서버 어딘가',
                            'comment': '오늘 밥먹음'
                        },
                        'additional': {
                            'description': '추가사항임'
                        }
                    },
                    '2days_ago': {
                        'date': '2018-09-07',
                        'meal': {
                            'breakfast': ['시리얼', '빵', '우유'],
                            'lunch': ['국수', '김치', '뭐시기', '오리'],
                            'dinner': ['고기', '깍두기', '음료수', '별로인거'],
                            'snack': '간식 먹지마'
                        },
                        'schedule': [{
                            'time': '09:00 ~ 10:00',
                            'work': '개발'
                        },
                            {
                                'time': '11:00 ~ 12:00',
                                'work': '잠'
                            }],
                        'condition': [
                            {
                                'low_temperature': True
                            },
                            {
                                'lose_Appetite': True
                            },
                            {
                                'human_power_reduction': True
                            }
                        ],
                        'photo': {
                            'photo_path': '서버 어딘가',
                            'comment': '오늘 밥먹음'
                        },
                        'additional': {
                            'description': '추가사항임'
                        }
                    }
                }
            }
        }
    }
}
