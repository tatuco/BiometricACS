from sqlalchemy import NVARCHAR, INTEGER, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from .BaseEntity import BaseEntity, Base


class Visit(Base):
    __tablename__ = 'visit'

    _id = Column('id', INTEGER, primary_key=True)
    _date_time = Column('date_time', TIMESTAMP, nullable=False)
    _event = Column('Event', NVARCHAR(500), nullable=False)
    _emp_id = Column('emp_id', INTEGER, ForeignKey('employee.id'), nullable=False)
    _camera_id = Column('camera_id', INTEGER, ForeignKey('camera.id'), nullable=False)

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def datetime(self):
        return self._date_time

    @datetime.setter
    def datetime(self, value):
        self._date_time = value

    @hybrid_property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    @hybrid_property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        if value > 0:
            self._emp_id = value

    @hybrid_property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        if value > 0:
            self._camera_id = value

    def __repr__(self):
        return "<Visit(id='%d', datetime='%s', event='%s',  emp_id='%d', camera_id='%d')>" % (self.id, self.datetime, self.event, self.emp_id, self.camera_id)