#!/usr/bin/python3
"""
script that lists all state objs containing the
letter 'a' from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """LINE LIMITS ARE FUN"""
    S = sessionmaker(bind=engine)
    s = S()

    states = s.query(State).filter(State.name.like('%a%'))\
                           .order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")