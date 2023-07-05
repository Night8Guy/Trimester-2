#!/usr/bin/python3
"""
script that changes the name of a state obj from database hbtn_0e_6_usa
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

    """I LOVE LINE LIMITS"""
    S = sessionmaker(bind=engine)
    s = S()

    state = s.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    s.commit()