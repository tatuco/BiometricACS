import pickle
import os


class Settings:

    def get_attrs(self):
        return list([f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('__')])

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

    def __init__(self, settings_file=None, backup_path=None, logs_path=None, trust_factor=None):
        self.settings_file = settings_file
        self.backup_path=backup_path
        self.logs_path=logs_path
        self.trust_factor=trust_factor
