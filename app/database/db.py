from threading import Lock
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from core import get_database_url


Base = declarative_base()

class Db():
    _instances = {}
    _lock : Lock = Lock
    _engine = None

    def __new__(cls, database="sqlite:///:memory:"):
        # Block other threads from creating a new object:
        with cls._lock():
            database = get_database_url() if get_database_url() else database
            if cls not in cls._instances:
                instance = super().__new__(cls)
                cls._instances[cls] = instance
                cls._engine = sa.create_engine(database)
                # Create tables (the database is temporary so everytime we start it we need to create all tables):
                Base.metadata.create_all(cls._engine)
        return cls._instances[cls]

    def __init__(self):
        # Create session (object to make queries):
        self.Session = sa.orm.sessionmaker(autocommit=False, bind=self._engine)

    def __enter__(self) -> sa.orm.Session:
        self.session = self.Session()
        return self.session
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.session.commit()
        except Exception as exception:
            self.session.rollback()
            raise exception
