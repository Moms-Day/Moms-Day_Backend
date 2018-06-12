def test_sample(flask_client):
    resp = flask_client.get('/index')

    assert resp.status_code == 200


def test_exit(user_dict):
    print(type(user_dict))
    assert user_dict['a'] == 1


def test_sample_post(flask_client, user_dict):
    resp = flask_client.post(
        '/index',
        json=user_dict
    )

    assert resp.status_code == 200
