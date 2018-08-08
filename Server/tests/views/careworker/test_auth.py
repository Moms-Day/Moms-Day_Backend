def test_auth_success(flask_client, info_test_care_worker):
    flask_client.post(
        '/care/signup',
        json=info_test_care_worker
    )

    resp = flask_client.post(
        'care/auth',
        json={
            'id': info_test_care_worker['id'],
            'pw': info_test_care_worker['pw']
        }
    )

    # status code 200
    assert resp.status_code == 200

    # Check if tokens is existence or nonexistence
    data = resp.json
    assert 'accessToken' in data
    assert 'refreshToken' in data

    # Check if tokens is str
    access = data['accessToken']
    refresh = data['refreshToken']

    assert type(access) is str
    assert type(refresh) is str


def test_auth_nonexistence_id(flask_client, info_test_care_worker):
    flask_client.post(
        'care/signup',
        json=info_test_care_worker
    )

    resp = flask_client.post(
        'care/auth',
        json={
            'id': info_test_care_worker['id'] + '11',
            'pw': info_test_care_worker['pw']
        }
    )

    # status code 401
    assert resp.status_code == 401


def test_auth_wrong_password(flask_client, info_test_care_worker):
    flask_client.post(
        'care/signup',
        json=info_test_care_worker
    )

    resp = flask_client.post(
        'care/auth',
        json={
            'id': info_test_care_worker['id'],
            'pw': info_test_care_worker['pw'] + 'wrong'
        }
    )

    # status code 401
    assert resp.status_code == 401
