#!/usr/bin/python3
"""
python file like model_state.py named model_city.py containing the class def of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
"""I dont think these two are needed, as well as the last two lines"""
from sqlalchemy import create_engine
import sys


class City(Base):
    """city class inherits from base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      autoincrement=True, nullable=False)

    engine = create_engine(f'mysql://{sys.argv[1]}:{sys.argv[2]}\
                           @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)