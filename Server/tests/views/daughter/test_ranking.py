import json

from app.models.facility import FacilityModel
from app.models.account import CareWorkerModel, DaughterModel


def test_facility_ranking_guest(flask_client):
    fac1 = FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    fac2 = FacilityModel(
        facility_code='00002',
        name='파주 요양병원',
        phone_number='03133332222',
        address='경기도 어딘가시 어딘가로',
        bio='일로오세염'
    ).save()

    examples = {
        'facilityRanking': [
            {
                'facilityCode': fac1.facility_code,
                'name': fac1.name,
                'address': fac1.address,
                'overall': fac1.overall if fac1.evaluation_count != 0 else None,
                'medals': fac1.medals
            },
            {
                'facilityCode': fac2.facility_code,
                'name': fac2.name,
                'address': fac2.address,
                'overall': fac2.overall if fac2.evaluation_count != 0 else None,
                'medals': fac2.medals
            }
        ]
    }

    resp = flask_client.get(
        '/daughter/ranking/facility'
    )

    # status code 200
    assert resp.status_code == 200

    # check response data
    assert examples == resp.json


def test_facility_ranking_member(flask_client, create_fake_daughter, create_fake_token):
    fac1 = FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    fac2 = FacilityModel(
        facility_code='00002',
        name='파주 요양병원',
        phone_number='03133332222',
        address='경기도 어딘가시 어딘가로',
        bio='일로오세염'
    ).save()

    care1 = CareWorkerModel(
        id='mlp123',
        pw='qwe123',
        name='김이박',
        phone_number='01099998888',
        career=2,
        patient_in_charge=3,
        facility_code='00003',
        bio='hi'
    ).save()

    DaughterModel.objects(id=create_fake_daughter.id).first().update(care_workers=[care1])

    examples = {
        'myFacilities': [
            {
                'facilityCode': fac1.facility_code,
                'name': fac1.name,
                'address': fac1.address,
                'overall': fac1.overall if fac1.evaluation_count != 0 else None,
                'medals': fac1.medals
            }
        ],
        'facilityRanking': [
            {
                'facilityCode': fac1.facility_code,
                'name': fac1.name,
                'address': fac1.address,
                'overall': fac1.overall if fac1.evaluation_count != 0 else None,
                'medals': fac1.medals
            },
            {
                'facilityCode': fac2.facility_code,
                'name': fac2.name,
                'address': fac2.address,
                'overall': fac2.overall if fac2.evaluation_count != 0 else None,
                'medals': fac2.medals
            }
        ]
    }

    resp = flask_client.get(
        '/daughter/ranking/facility',
        headers={'Authorization': create_fake_token['d_access']}
    )

    # status code 200
    assert resp.status_code == 200

    # check response data
    assert examples == resp.json


def test_care_worker_ranking_guest(flask_client):
    FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    FacilityModel(
        facility_code='00002',
        name='파주 요양병원',
        phone_number='03133332222',
        address='경기도 어딘가시 어딘가로',
        bio='일로오세염'
    ).save()

    care1 = CareWorkerModel(
        id='mlp123',
        pw='qwe123',
        name='김이박',
        phone_number='01099998888',
        career=2,
        patient_in_charge=3,
        facility_code='00003',
        bio='hi',
        overall=4,
        evaluation_count=1
    ).save()

    care2 = CareWorkerModel(
        id='cde321',
        pw='yyy111',
        name='최정',
        phone_number='01079998288',
        career=10,
        patient_in_charge=5,
        facility_code='00002',
        bio='hello'
    ).save()

    resp = flask_client.get(
        '/daughter/ranking/care_worker'
    )

    examples = {
        'careWorkerRanking': [
            {
                'careWorkerId': care1.id,
                'name': care1.name,
                'workplace': FacilityModel.objects(facility_code=care1.facility_code).first().name,
                'patientInCharge': care1.patient_in_charge,
                'career': care1.career,
                'overall': round(care1.overall / care1.evaluation_count, 1)
            },
            {
                'careWorkerId': care2.id,
                'name': care2.name,
                'workplace': FacilityModel.objects(facility_code=care2.facility_code).first().name,
                'patientInCharge': care2.patient_in_charge,
                'career': care2.career,
                'overall': None
            }
        ]
    }

    # status code 200
    assert resp.status_code == 200

    # check response data
    assert examples == resp.json


def test_care_worker_ranking_member(flask_client, create_fake_daughter, create_fake_token):
    FacilityModel(
        facility_code='00003',
        name='인천 요양병원',
        phone_number='021120000',
        address='인천광역시 입구 봄동',
        bio='시설 짱짱 좋아요 여기 ㅎㅎ',
        overall=5,
        evaluation_count=1,
        medals=['crazy', 'awesome', 'amazing']
    ).save()

    FacilityModel(
        facility_code='00002',
        name='파주 요양병원',
        phone_number='03133332222',
        address='경기도 어딘가시 어딘가로',
        bio='일로오세염'
    ).save()

    care1 = CareWorkerModel(
        id='mlp123',
        pw='qwe123',
        name='김이박',
        phone_number='01099998888',
        career=2,
        patient_in_charge=3,
        facility_code='00003',
        bio='hi',
        overall=4,
        evaluation_count=1
    ).save()

    DaughterModel.objects(id=create_fake_daughter.id).first().update(care_workers=[care1])

    care2 = CareWorkerModel(
        id='cde321',
        pw='yyy111',
        name='최정',
        phone_number='01079998288',
        career=10,
        patient_in_charge=5,
        facility_code='00002',
        bio='hello'
    ).save()

    examples = {
        'myCareWorkers': [
            {
                'careWorkerId': care1.id,
                'name': care1.name,
                'workplace': FacilityModel.objects(facility_code=care1.facility_code).first().name,
                'patientInCharge': care1.patient_in_charge,
                'career': care1.career,
                'overall': round(care1.overall / care1.evaluation_count, 1)
            }
        ],
        'careWorkerRanking': [
            {
                'careWorkerId': care1.id,
                'name': care1.name,
                'workplace': FacilityModel.objects(facility_code=care1.facility_code).first().name,
                'patientInCharge': care1.patient_in_charge,
                'career': care1.career,
                'overall': round(care1.overall / care1.evaluation_count, 1)
            },
            {
                'careWorkerId': care2.id,
                'name': care2.name,
                'workplace': FacilityModel.objects(facility_code=care2.facility_code).first().name,
                'patientInCharge': care2.patient_in_charge,
                'career': care2.career,
                'overall': None
            }
        ]
    }

    resp = flask_client.get(
        '/daughter/ranking/care_worker',
        headers={'Authorization': create_fake_token['d_access']}
    )

    # status code 200
    assert resp.status_code == 200

    # check response data
    assert examples == resp.json
