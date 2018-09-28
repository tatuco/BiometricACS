from zope.interface import Interface, implementer


class IRepository(Interface):

    def get_all(self):
        pass

    def get(self, item_id):
        pass

    def find(self, predicate):
        pass

    def create(self, item):
        assert isinstance(item, self)

    def update(self, item):
        assert isinstance(item, self)

    def delete(self, item):
        assert isinstance(item, self)
