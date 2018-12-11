import os
import re
import pickle

from ..DTO import AccountDTO, EnumsDTO
from ...DAL import EntitiesUnit, Account


class Settings:

    def get_attrs(self):
        return list([f for f in dir(self) if not callable(getattr(self, f)) and not f.startswith('_') and f != 'cfg_file'])

    def update_obj(self, item):
        attr = self.get_attrs()
        for a in attr:
            self.__setattr__(a, item.__getattribute__(a))
        return self

    def save(self):
        options = []
        if self.settings_file:
            for attr in self.get_attrs():
                options.append(self.__getattribute__(attr))
            with open(self.settings_file, 'wb') as f:
                pickle.dump(options, f)

    def copy_settings_to_file(self, file_name):
        previous_settings_file = self.settings_file
        self.settings_file = os.path.abspath(file_name)
        self.save()
        self.settings_file = os.path.abspath(previous_settings_file)

    def restore(self):
        if self.settings_file:
            with open(self.settings_file, 'rb') as f:
                options = pickle.load(f)
                for (o, attr) in zip(options, self.get_attrs()):
                    self.__setattr__(attr, o)

    def forced_restore(self, settings_file, previous_settings_file):
        self.settings_file = settings_file
        try:
            self.restore()
        except Exception:
            self.settings_file = previous_settings_file
            try:
                self.restore()
            except Exception:
                if os.path.exists(self.settings_file):
                    os.remove(self.settings_file)
                new_settings = Settings()
                new_settings.save()
                self.update_obj(new_settings)
            return False
        with open(self.cfg_file, 'wb') as f:
            pickle.dump(self.settings_file, f)
        return True

    def parse_connection_string(self, connection_string):
        r_user = r'://([\s\S]+?):'
        user = re.findall(r_user, connection_string)[0]
        r_password = rf'://' + user + ':([\s\S]+?)@'
        password = re.findall(r_password, connection_string)
        try:
            password = password[0]
        except Exception:
            password = user
        account = AccountDTO(user, password, role=EnumsDTO.AccountRoleDTO.technical_engineer)
        try:
            db = EntitiesUnit(connection_string)
            db.account_repository.create(account)
            db.save()
            return account
        except Exception:
            return None

    def is_valid_connection(self, conn):
        return EntitiesUnit.is_valid_connection(conn)

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

    def __init__(self, settings_file='.\.\APP\Sources\Settings.set', backup_path='.\.\APP\Sources\Backups', logs_path='.\.\APP\Sources\Logs', logs_saving=True, truth_factor=0.9, square_coef=0.7,
                 connection_string='',
                 language='ru-RU'):
        self.settings_file = os.path.abspath(settings_file)
        self.backup_path = os.path.abspath(backup_path)
        self.logs_path = os.path.abspath(logs_path)
        self.logs_saving = logs_saving
        self.truth_factor = truth_factor
        self.square_coef = square_coef
        self.connection_string = connection_string
        self._cfg_path = '.\.\APP\Sources\Sys\sys.cfg'
        self.language = language
