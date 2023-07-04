#!/usr/bin/python3
"""
script that adds the state obj 'Louisiana' to database hbtn_0e_6_usa
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

    S = sessionmaker(bind=engine)
    s = S()

    state_name = State(name="Louisiana")
    s.add(state_name)
    s.commit()

    print(state_name.id)