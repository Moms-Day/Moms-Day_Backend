import pytest
import pymongo

from flask_jwt_extended import create_access_token, create_refresh_token

from app import create_app
from config.test import TestConfig

from app.models.account import CareWorkerModel, DaughterModel
from app.models.patient import PatientModel


@pytest.fixture(scope='session')
def flask_app():
    """
    Provide flask instance for test
        return: Flask instance
        teardown: pop at context
    """
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()

    yield app

    # teardown
    app_context.pop()


@pytest.fixture(scope='session')
def flask_client(flask_app):
    """
    Provide flask testing client
        param: flask_app - fixture
        return: flask testing client
    """
    return flask_app.test_client()


@pytest.fixture(scope="function")
def mongodb_set_for_test(flask_app):
    """
    Create Mongodb client for drop database
        param: flask_app - fixture
        return: mongodb client
        teardown: drop database
    """
    mongo_setting = flask_app.config['MONGODB_SETTINGS']
    db_name = mongo_setting.pop('db')
    mongo_client = pymongo.MongoClient(**mongo_setting)
    mongo_setting['db'] = db_name

    return mongo_client, db_name


@pytest.fixture(scope="function")
def info_test_care_worker(mongodb_set_for_test):
    """
    Provide fake user information
        return: fake CareWorker info for testing
    """
    yield {
        "id": "flouie74",
        "pw": "qqweq1",
        "name": "jks",
        "career": 4,
        "patientInCharge": 2,
        "phoneNumber": "01011112222",
        "certifyCode": "jcnqj3nd23i13",
        "facilityCode": "111qqq222www",
        "bio": "I'm seung yung"
    }

    mongodb_set_for_test[0].drop_database(mongodb_set_for_test[1])


@pytest.fixture(scope="function")
def info_test_daughter(mongodb_set_for_test):
    """
    Provide fake user information
        return: fake Daughter info for testing
    """
    yield {
        "id": "rudtj2316",
        "pw": "zaq123",
        "phoneNumber": "01033334444",
        "certifyCode": "fmrkfmk3132",
        "name": "jyj",
        "age": 25,
        "parents": [
            {"name": "kdi", "age": 65, "gender": False},
            {"name": "lpp", "age": 72, "gender": True}
        ]
    }

    mongodb_set_for_test[0].drop_database(mongodb_set_for_test[1])


@pytest.fixture()
def create_fake_daughter(info_test_daughter, mongodb_set_for_test):
    pn, cc = info_test_daughter.pop('phoneNumber'), info_test_daughter.pop('certifyCode')
    info_test_daughter['phone_number'], info_test_daughter['certify_code'] = pn, cc
    parents = info_test_daughter.pop('parents')

    daughter = DaughterModel(**info_test_daughter).save()
    for p in parents:
        PatientModel(name=p['name'], age=p['age'], gender=['gender'], daughter=daughter).save()

    yield daughter

    mongodb_set_for_test[0].drop_database(mongodb_set_for_test[1])


@pytest.fixture()
def create_fake_token(flask_app, create_fake_daughter):
    with flask_app.app_context():
        daughter_access_token = 'JWT {}'.format(create_access_token(create_fake_daughter.id))
        daughter_refresh_token = 'JWT {}'.format(create_refresh_token(create_fake_daughter.id))

    return {
        'd_access': daughter_access_token,
        'd_refresh': daughter_refresh_token
    }
