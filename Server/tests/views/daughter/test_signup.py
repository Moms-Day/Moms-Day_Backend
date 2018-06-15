def test_signup_success(flask_client, mongodb_set_for_test, info_test_daughter):
    resp = flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    # status code 201
    assert resp.status_code == 201

    # DaughterModel 에 잘 들어 갔는지 확인 (DaughterModel 의 Document 에서 추가한 PatientModel 의 Document 를 참조하는지도)


def test_id_duplicated(flask_client, mongodb_set_for_test, info_test_daughter):
    flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    resp = flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    # status code 409
    assert resp.status_code == 409

    # Check message
    assert resp.json['msg'] == 'id duplicated'


def incorrect_certify_code():
    pass
