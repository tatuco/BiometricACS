from abc import abstractmethod


class Observer:

    @abstractmethod
    def model_is_changed(self):
        pass
