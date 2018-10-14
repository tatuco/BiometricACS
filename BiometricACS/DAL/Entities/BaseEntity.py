from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseEntity:

    @hybrid_property
    def id(self):
        return self._id

    def update(self, item):
        attr = [f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('__') and not f.startswith('_') and f != 'id' and f != 'metadata']
        # assert isinstance(item, type(self))
        for a in attr:
            self.__setattr__(a, item.__getattribute__(a))
        return self

    def __repr__(self):
        repr_str = '<' + type(self).__name__ + '('
        attr = [f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('__') and not f.startswith('_') and f != 'metadata']
        for a in range(len(attr)):
            repr_str += attr[a] + "='" + str(self.__getattribute__(attr[a]))
            if a != len(attr)-1:
                repr_str += "', "
                continue
            repr_str += "')>"
        return repr_str
