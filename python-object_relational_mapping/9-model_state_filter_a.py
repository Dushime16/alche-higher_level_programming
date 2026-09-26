#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db_name
            ),
            pool_pre_ping=True
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(
            State.name.like('%a%')
        ).order_by(State.id.asc()).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))

        session.close()
