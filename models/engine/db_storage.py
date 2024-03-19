#!/usr/bin/python3
"""

"""



from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = ("HBNB_ENV")

        self.__engine = create_engine(f"mysql+mysqldb://\
                                    {user}:{passwd}@{host}/{database}",
                                    pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import base_model
        # self.__session()

        session = self.__session
        if cls:
            return session.query(cls).all()
        else:
            classes = [getattr(base_model, c) for c in dir(base_model)
                       is isinstance(getattr(base_model, c), type)]
        objects = {}
        for cls in classes:
            objects.extend(session.query(cls).all())
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit(self)

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        self.__session.close()

