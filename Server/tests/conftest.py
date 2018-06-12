import pytest
import pymongo

from app import create_app
from config.test import TestConfig


@pytest.fixture(scope='session')
def flask_app():
    """"""
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()

    yield app

    # teardown
    app_context.pop()


@pytest.fixture(scope='session')
def flask_client(flask_app):
    return flask_app.test_client()


# pytest 의 fixture 는 scope 밖으로 벗어나면 최종화(teardown) 코드를 실행하도록 도와주는데, 이 때 return 이 아닌 yield 를 이용한다.
# yield 뒤 모든 코드가 teardown 코드가 된다.
@pytest.fixture(scope="session")
def mongodb_set_for_test(flask_app):
    mongo_setting = flask_app.config['MONGODB_SETTINGS']
    db_name = mongo_setting.pop('db')
    mongo_client = pymongo.MongoClient(**mongo_setting)
    mongo_setting['db'] = db_name

    yield mongo_client

    # teardown
    mongo_client.drop_database(db_name)


@pytest.fixture()
def info_test_user():
    return {
        "id": "flouie74",
        "pw": "qqweq1",
        "name": "jks",
        "career": 4,
        "patientInCharge": 2,
        "phoneNumber": "01090721383",
        "certifyCode": "jcnqj3nd23i13",
        "facilityCode": "111qqq222www",
        "bio": "I'm seung yung"
    }


@pytest.fixture()
def user_dict():
    return {'a': 1, 'b': 2}
