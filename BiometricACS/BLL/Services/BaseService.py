class BaseService:
    _mObservers = []

    def add_observer(self, inObserver):
        self._mObservers.append(inObserver)

    def remove_observer(self, inObserver):
        self._mObservers.remove(inObserver)

    def notify_observers(self):
        for o in self._mObservers:
            o.model_is_changed()