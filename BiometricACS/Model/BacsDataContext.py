from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BacsDataContext():
    _connection_string = 'postgresql://postgres:123@localhost:5432/postgres'

    @property
    def connection_string(self):
        return self._connection_string

    @connection_string.setter
    def connection_string(self, value):
        if value not in [None, ''] and value != self._connection_string:
            self._connection_string = value
            self.refresh_engine()

    def refresh_engine(self):
        self.session = sessionmaker()
        engine = create_engine(self._connection_string)
        self.session.configure(bind=engine)

    def __init__(self):
        sess = sessionmaker()
        engine = create_engine(self._connection_string)
        sess.configure(bind=engine)
        self.session = sess()
