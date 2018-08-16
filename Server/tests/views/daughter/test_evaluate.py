from app.models.facility import FacilityModel


def test_facility_evaluate_success(flask_client, create_fake_token):
    fac = FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    resp = flask_client.patch(
        '/daughter/evaluate/facility/{}'.format(fac.facility_code),
        headers={'Authorization': create_fake_token['d_access']},
        json={
            'equipment': 4,
            'meal': 4,
            'schedule': 4,
            'cost': 4,
            'service': 4,
            'overall': 4.0,
            'lineE': 'awesome'
        }
    )

    # status code 200
    assert resp.status_code == 201


def test_facility_evaluate_nonexistence_id(flask_client, create_fake_token):
    fac = FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    resp = flask_client.patch(
        '/daughter/evaluate/facility/{}'.format(str(int(fac.facility_code) + 5)),
        headers={'Authorization': create_fake_token['d_access']},
        json={
            'equipment': 4,
            'meal': 4,
            'schedule': 4,
            'cost': 4,
            'service': 4,
            'overall': 4.0,
            'lineE': 'awesome'
        }
    )

    # status code 200
    assert resp.status_code == 400


def test_care_worker_evaluate_success(flask_client, create_fake_care_worker, create_fake_token):
    resp = flask_client.patch(
        '/daughter/evaluate/care_worker/{}'.format(create_fake_care_worker.id),
        headers={'Authorization': create_fake_token['d_access']},
        json={
            'diligence': 3,
            'kindness': 3,
            'overall': 3.0,
            'lineE': 'holy'
        }
    )

    assert resp.status_code == 201


def test_care_worker_evaluate_nonexistence_id(flask_client, create_fake_care_worker, create_fake_token):
    resp = flask_client.patch(
        '/daughter/evaluate/care_worker/{}'.format(create_fake_care_worker.id + '5'),
        headers={'Authorization': create_fake_token['d_access']},
        json={
            'diligence': 3,
            'kindness': 3,
            'overall': 3.0,
            'lineE': 'holy'
        }
    )

    assert resp.status_code == 400
