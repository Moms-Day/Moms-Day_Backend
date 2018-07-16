from werkzeug.security import check_password_hash

from app.models.account import CareWorkerModel


def test_signup_success(flask_client, mongodb_set_for_test, info_test_care_worker):
    mongodb_set_for_test.drop_database("Mom's_day")
    resp = flask_client.post(
        '/care/signup',
        json=info_test_care_worker
    )

    # status code 201
    assert resp.status_code == 201

    # Check that if data inserted the database
    new_worker = CareWorkerModel.objects(id=info_test_care_worker['id']).first()
    assert new_worker is not None

    assert new_worker.id == info_test_care_worker['id']
    assert check_password_hash(new_worker.pw, info_test_care_worker['pw'])
    assert new_worker.name == info_test_care_worker['name']
    assert new_worker.career == info_test_care_worker['career']
    assert new_worker.patient_in_charge == info_test_care_worker['patientInCharge']
    assert new_worker.phone_number == info_test_care_worker['phoneNumber']
    assert new_worker.certify_code == info_test_care_worker['certifyCode']
    assert new_worker.facility_code == info_test_care_worker['facilityCode']
    assert new_worker.bio == info_test_care_worker['bio']


def test_id_duplicated(flask_client, mongodb_set_for_test, info_test_care_worker):
    flask_client.post(
        '/care/signup',
        json=info_test_care_worker
    )

    resp = flask_client.post(
        '/care/signup',
        json=info_test_care_worker
    )

    # status code 409
    assert resp.status_code == 409


def incorrect_facility_code():
    pass


def incorrect_certify_code():
    pass
