#!/usr/bin/python3

from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """A class for managing storage with SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Create engine and session"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query on the current database session"""
        from model import classes
        objs = {}
        if cls:
            for obj in self.__session.query(classes[cls]).all():
                key = '{}.{}'.format(cls, obj.id)
                objs[key] = obj
        
        else:
            for cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = '{}.{}'.format(cls, obj,id)
                    objs[key] = obj
                return objs
            
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

storage = DBStorage()
storage.reload()
