from ..BusinessModels.Settings import Settings


class SettingsDTO:

    def get_attrs(self):
        return list([f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('_') and f != 'cfg_file'])

    def update_obj(self, item):
        attr = self.get_attrs()
        for a in attr:
            self.__setattr__(a, item.__getattribute__(a))
        return self

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

    def __init__(self,):
        self.settings_file = None
        self.backup_path = None
        self.logs_path = None
        self.logs_saving = None
        self.truth_factor = None
        self.square_coef = None
        self.connection_string = None
        self.language = None
