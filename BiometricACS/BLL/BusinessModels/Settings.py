import pickle
import os


class Settings:

    def get_attrs(self):
        return list([f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('_') and f != 'cfg_file'])

    def save(self):
        options = []
        if self.settings_file:
            for attr in self.get_attrs():
                options.append(self.__getattribute__(attr))
            with open(self.settings_file, 'wb') as f:
                pickle.dump(options, f)

    def restore(self):
        if self.settings_file:
            with open(self.settings_file, 'rb') as f:
                options = pickle.load(f)
                for (o, attr) in zip(options, self.get_attrs()):
                    self.__setattr__(attr, o)

    @property
    def cfg_file(self):
        return self._cfg_path

    def __repr__(self):
        repr_str = '<' + type(self).__name__ + '('
        attr = self.get_attrs()
        for a in range(len(attr)):
            repr_str += attr[a] + "='" + str(self.__getattribute__(attr[a]))
            if a != len(attr) - 1:
                repr_str += "', "
                continue
            repr_str += "')>"
        return repr_str

    def __init__(self, settings_file='.\.\APP\Sources\Settings', backup_path=None, logs_path='.\.\APP\Sources\Logs', logs_saving=True, truth_factor=0.9, square_coef=0.7, connection_string=None):
        self.settings_file = settings_file
        self.backup_path = backup_path
        self.logs_path = logs_path
        self.logs_saving = logs_saving
        self.truth_factor = truth_factor
        self.square_coef = square_coef
        self.connection_string = connection_string
        self._cfg_path = '.\.\APP\Sources\Sys\cfg'
