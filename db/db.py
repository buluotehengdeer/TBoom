from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cnf.settings import Settings
from sqlalchemy.orm import sessionmaker

# 创建数据库访问引擎
engine = create_engine(Settings.DATABASE,
                       encoding='utf-8', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(64))
    score = Column(Integer, nullable=True)

Base.metadata.create_all(engine)


def insertData(username, password, engine=engine):
    '''
        插入数据
    '''
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    user_obj = User(username=username, password=password)
    Session.add(user_obj)
    Session.commit()


def queryData(username, password, engine=engine):
    '''
        查找数据
    '''
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    user = Session.query(User).filter_by(
        username=username).filter_by(password=password).first()
    return user


def isExist(username, engine=engine):
    '''
        判断用户名是否存在

    '''
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    user = Session.query(User).filter_by(
        username=username).first()
    return user


def updateScore(username, score, engine=engine):
    '''
        更新分数
    '''
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    user = Session.query(User).filter_by(username=username).first()
    if user.score is None:
        user.score = score
    elif user.score < score:
        user.score = score
    Session.commit()


def getRank(engine=engine):
    '''
        获得排行榜
        Rerurns:
            [(username,socre)....]
    '''
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    rank = Session.query(User).order_by(User.score.desc()).all()
    rank_result = []
    for r in rank:
        rank_result.append((r.username, r.score))
    return rank_result
