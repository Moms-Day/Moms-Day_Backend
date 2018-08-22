import socket

from config import Config


class ProductionConfig(Config):
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = False

    IMAGE_PATH_FOR_DOWNLOAD = HOST + '/statics/imgs'

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })

    Config.SWAGGER['host'] = '{}:{}'.format(Config.DOMAIN or HOST, PORT)
