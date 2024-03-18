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
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = ("HBNB_MYSQL_DB")
        env = ("HBNB_ENV")

        self.__engine = create_engine(f"mysql+mysqldb://\
                                    {user}:{passwd}@{host}/{database}",
                                    pool_pre_ping=True)

        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        # self.__session()

        obj_dictionary = {}
        if not cls:
            cls_list = [User, State, City, Amenity, Place, Review]
            query_list = []
            for cls_name in cls_list:
                query_list.extend(self.__session.query(cls_name).all())
        else:
            query_list = self.__session.query(cls).all()
            for obj in query_list:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dictionary[key] = obj

        return (obj_dictionary)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit(self)

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        self.__session.close()

