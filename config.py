user_name = ''
password = ''
db_name = ''

class Config(object):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user_name}:{password}@localhost/{db_name}'
