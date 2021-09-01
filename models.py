from app import app
from datetime import date
from contextlib import contextmanager
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Date,Boolean,Text
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# first_table user_id, name, middle_name, bornDate, gender
# user_id, education, comment, citizenship

Base = declarative_base(app.config['SQLALCHEMY_DATABASE_URI'])




@contextmanager
def db_session(db_url):
    engine = create_engine(db_url,client_encoding='utf8')

    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    yield db_session
    db_session.close()
    connection.close()




class PersonBase(Base):
    __tablename__ = 'base_user'
    user_id  = Column(Integer,primary_key=True)
    name = Column(String(100))
    middle_name  = Column(String(100))
    born_date = Column(Date)
    gender = Column(String(100))
    addition_info = relationship('AdditionPersonBase',backref='pers_stat',lazy=True)
    phone_info = relationship('Phone',backref='phones',lazy=True)

class AdditionPersonBase(Base):
    __tablename__ = 'addition_person_base'
    user_id = Column(Integer, primary_key=True)
    education = Column(String(255))
    citizen = Column(Boolean)
    comment = Column(Text)
    id = Column(Integer, ForeignKey('base_user.user_id'), nullable=False)

class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer,primary_key=True)
    phone = Column(String(100))
    phone_id = Column(Integer,ForeignKey('base_user.user_id'),nullable=False)





