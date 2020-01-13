import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

# engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost:3306/lesson-service', echo=True)
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost/lesson-service?host=localhost?port=33066",
                                  echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def get_session() -> Session:
    return Session()
