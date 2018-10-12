from datetime import datetime
from ..BLL.BusinessModels import Settings
from .Subsystems import ProgramLogging

program_settings = Settings()
program_logs = ProgramLogging(lambda x: x)

