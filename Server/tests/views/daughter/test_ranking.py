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
                'overall': fac1.overall,
                'medals': fac1.medals
            },
            {
                'facilityCode': fac2.facility_code,
                'name': fac2.name,
                'address': fac2.address,
                'overall': fac2.overall,
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
                'overall': fac1.overall,
                'medals': fac1.medals
            }
        ],
        'facilityRanking': [
            {
                'facilityCode': fac1.facility_code,
                'name': fac1.name,
                'address': fac1.address,
                'overall': fac1.overall,
                'medals': fac1.medals
            },
            {
                'facilityCode': fac2.facility_code,
                'name': fac2.name,
                'address': fac2.address,
                'overall': fac2.overall,
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
