#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
import models
from models.clas import Clas
from models.institution import Institution
from models.subject import Subject
from models.teacher import Teacher
from models.lesson import Lesson
from models.state import State
from models.city import City
from models.student import Student


classes = {'Institution': Institution, 'Subject': Subject,
           'Teacher': Teacher, 'Lesson': Lesson, 'Class': Clas,
           'State': State, 'City': City, 'Student': Student}
dotenv_path = find_dotenv()
# print(f"Loading .env file from: {dotenv_path}")
load_dotenv(dotenv_path)


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ACME_MYSQL_USER = getenv('u')
        ACME_MYSQL_PWD = getenv('p')
        ACME_MYSQL_HOST = getenv('h')
        ACME_MYSQL_DB = getenv('D')
        ACME_ENV = getenv('mode')
        CHARSET_STR = '?charset=utf8mb4'

        # print(f"user: {ACME_MYSQL_USER}\npassword: {ACME_MYSQL_PWD}\nhost: {ACME_MYSQL_HOST}\ndatabase: {ACME_MYSQL_DB}")
        if None in (ACME_MYSQL_USER, ACME_MYSQL_PWD,
                    ACME_MYSQL_HOST, ACME_MYSQL_DB):
            string = "One or more required environment variables are not set."
            raise ValueError(string)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}{}'.
                                      format(ACME_MYSQL_USER,
                                             ACME_MYSQL_PWD,
                                             ACME_MYSQL_HOST,
                                             ACME_MYSQL_DB,
                                             CHARSET_STR),
                 # Recycle connections older than 1 hour, to avoid times-out
                                      pool_recycle=3600,
                                      connect_args={"connect_timeout": 10})
        if not database_exists(self.__engine.url):
            # Create the database
            create_database(self.__engine.url)

        if ACME_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def query(self, cls):
        """ give access to the current session outside this module"""
        return self.__session.query(cls)

    def rollback(self):
        """rollback"""
        self.__session.rollback()
