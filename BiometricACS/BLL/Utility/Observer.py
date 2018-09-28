from abc import abstractmethod

class Observer():
    """Docs for LoginPanelObserver"""

    @abstractmethod
    def modelIsChanged(self):
        pass