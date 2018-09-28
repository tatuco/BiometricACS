class BaseViewModel:
    _mObservers = []

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self):
        for o in self._mObservers:
            o.modelIsChanged()