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

    Config.SWAGGER['host'] = '{}:{}'.format(Config.DOMAIN or HOST, PORT)
