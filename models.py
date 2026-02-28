from enum import unique

import flask_login
from sqlalchemy import Column, DateTime, func, ForeignKey, Integer, String, create_engine,Text
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from flask_login import UserMixin

engine = create_engine('mysql+pymysql://root:@localhost:3306/rpg')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Player(Base,UserMixin):
    id_p = Column(Integer, primary_key=True)
    nome = Column(String,unique=True, nullable=False)
    nome = Column(String,unique=True, nullable=False)
    nome = Column(String,unique=True, nullable=False)
    nome = Column(String,unique=True, nullable=False)
    nome = Column(String,unique=True, nullable=False)
    nome = Column(String,unique=True, nullable=False)

class Saves(Base,UserMixin):