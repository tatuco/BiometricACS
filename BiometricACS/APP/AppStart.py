from datetime import datetime
from ..BLL.BusinessModels import Settings, ProgramLogs, Log

program_settings = Settings()
program_logs = ProgramLogs(Log(datetime.now(), 'Initialize program components'))