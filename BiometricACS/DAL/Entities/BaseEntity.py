from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseEntity():
    def update(self, item):
        attr = [f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('__') and not f.startswith('_') and f != 'id' and f != 'metadata']
        assert isinstance(item, type(self))
        for a in attr:
            self.__setattr__(a, item.__getattribute__(a))
