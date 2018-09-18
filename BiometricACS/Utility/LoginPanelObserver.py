from abc import ABCMeta, abstractmethod

class LoginPanelObserver(metaclass=ABCMeta):
    """Docs for LoginPanelObserver"""

    @abstractmethod
    def modelIsChanged(self):
        pass
        
        