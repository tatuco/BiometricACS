from zope.interface import Interface, implementer


class IEntitiesUnit(Interface):

    def save(self):
        pass