from sqlalchemy import NVARCHAR, INTEGER, Enum
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property

from .EnumModels import AccountRole
from .BaseEntity import BaseEntity, Base


class Account(Base, BaseEntity):
    __tablename__ = 'account'

    _id = Column('id', INTEGER, primary_key=True)
    _username = Column('username', NVARCHAR(100), nullable=False, unique=True)
    _password = Column('password', NVARCHAR(40), nullable=False)
    _role = Column('role', Enum(AccountRole), nullable=False)

    @hybrid_property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value not in [None, '']:
            self._username = value

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value not in [None, '']:
            self._password = value

    @hybrid_property
    def role(self):
        return self._role

    @role.setter
    def role(self, vale):
        if vale in list(AccountRole):
            self._role = vale