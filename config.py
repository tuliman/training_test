data = []
with open('config',mode='r')as conf:

    for var in conf:
        data.append(var.rstrip())

user_name,password,db_name = data
print(user_name,password,db_name)

class Config(object):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user_name}:{password}@localhost/{db_name}'
    print(SQLALCHEMY_DATABASE_URI)
