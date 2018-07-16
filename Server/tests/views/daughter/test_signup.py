from werkzeug.security import check_password_hash

from app.models.account import DaughterModel
from app.models.patient import PatientModel


def test_signup_success(flask_client, mongodb_set_for_test, info_test_daughter):
    mongodb_set_for_test.drop_database("Mom's_day")
    resp = flask_client.post(
        '/daughter/signup',
        json=info_test_daughter
    )

    # status code 201
    assert resp.status_code == 201

    # -----Check that if data inserted the database-----
    # 1. DaughterModel
    new_user = DaughterModel.objects(id=info_test_daughter['id']).first()
    assert new_user is not None

    assert new_user.id == info_test_daughter['id']
    assert check_password_hash(new_user.pw, info_test_daughter['pw'])
    assert new_user.phone_number == info_test_daughter['phoneNumber']
    assert new_user.certify_code == info_test_daughter['certifyCode']
    assert new_user.name == info_test_daughter['name']
    assert new_user.age == info_test_daughter['age']

    # 2. PatientModel
    new_p = PatientModel.objects(daughter=new_user.id)
    req_p = info_test_daughter['parents']

    assert len(new_p) == len(req_p)

    assert new_p[0].name == req_p[0]['name']
    assert new_p[0].age == req_p[0]['age']
    assert new_p[0].gender == req_p[0]['gender']

    assert new_p[1].name == req_p[1]['name']
    assert new_p[1].age == req_p[1]['age']
    assert new_p[1].gender == req_p[1]['gender']


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


def incorrect_certify_code():
    pass
