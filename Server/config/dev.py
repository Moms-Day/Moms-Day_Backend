from config import Config


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 7070
    DEBUG = True

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })

    MONGODB_SETTINGS = dict(Config.MONGODB_SETTINGS, **{
        'host': HOST,
    })

    Config.SWAGGER['host'] = '{}:{}'.format(Config.DOMAIN or HOST, PORT)
