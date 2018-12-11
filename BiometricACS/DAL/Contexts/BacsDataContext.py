from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..Entities import *


class BacsDataContext:

    def set_context(self):
        self.Account = self.sess.query(Account)
        self.Biometric = self.sess.query(Biometrics)
        self.Camera = self.sess.query(Camera)
        self.Checkpoint = self.sess.query(Checkpoint)
        self.Department = self.sess.query(Department)
        self.Employee = self.sess.query(Employee)
        self.Visit = self.sess.query(Visit)

    def __init__(self, connection_string):
        sess = sessionmaker()
        engine = create_engine(connection_string)
        sess.configure(bind=engine)
        self.sess = sess()
        self.Account = None
        self.Biometric = None
        self.Camera = None
        self.Checkpoint = None
        self.Department = None
        self.Employee = None
        self.Visit = None
        self.set_context()

