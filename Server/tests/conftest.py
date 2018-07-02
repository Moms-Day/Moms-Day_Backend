import pytest
import pymongo

from app import create_app
from config.test import TestConfig


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


@pytest.fixture(scope="session")
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

    yield mongo_client

    # teardown
    mongo_client.drop_database(db_name)


@pytest.fixture(scope="function")
def info_test_care_worker():
    """
    Provide fake user information
        return: fake CareWorker info for testing
    """
    return {
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


@pytest.fixture(scope="function")
def info_test_daughter():
    """
    Provide fake user information
        return: fake Daughter info for testing
    """
    return {
        "id": "rudtj2316",
        "pw": "zaq123",
        "name": "jyj",
        "age": 25,
        "phoneNumber": "01033334444",
        "certifyCode": "fmrkfmk3132",
        "patients": [
            {"name": "kdi", "age": 65, "gender": False},
            {"name": "lpp", "age": 72, "gender": True}
        ]
    }
