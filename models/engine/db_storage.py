#!/usr/bin/python3
"""

"""



from sqlalchemy import create_engine
from os import getenv
import sys
from models.base_model import Base, BaseModel
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
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        # print(user, passwd, host, database, env)

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@{host}/{database}",
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = getattr(sys.modules[__name__], cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

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

