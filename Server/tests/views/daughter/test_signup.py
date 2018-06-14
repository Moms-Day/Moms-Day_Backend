def test_signup_success(flask_client, mongodb_set_for_test, info_test_daughter):
    resp = flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    # status code 201
    assert resp.status_code == 201

    # Check that if data inserted the database
    # assert CareWorkerModel.objects(id=info_test_care_worker['id']).first() is not None


def test_id_duplicated(flask_client, mongodb_set_for_test, info_test_daughter):
    flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    resp = flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )
