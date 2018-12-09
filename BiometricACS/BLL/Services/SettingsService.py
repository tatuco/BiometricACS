import glob
import os

from .BaseService import BaseService
from ..DTO import SettingsDTO
from ...DAL import EntitiesUnit


class SettingsService(BaseService):

    def get_locales(self):
        locales = glob.glob('./APP/Locale/??-??')
        return [os.path.basename(locale) for locale in locales]

    def is_valid_values(self):
        if self.settings.truth_factor <= 0 or self.settings.truth_factor > 1:
            return False
        if self.settings.square_coef <= 0 or self.settings.square_coef > 1:
            return False
        return True

    def is_valid_paths(self):
        if not self.settings.logs_path or not self.settings.backup_path or not self.settings.settings_file:
            return False
        return True

    def is_valid_conn_str(self):
        return EntitiesUnit.is_valid_connection(self.settings.connection_string)

    def __init__(self, s):
        super().__init__()
        self.settings = SettingsDTO().update_obj(s)
