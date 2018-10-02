class ProgramLogs:

    @property
    def logs(self):
        return self._logs

    def add_log(self, log):
        self._logs.append(log)

    def __init__(self, first_log=None):
        self._logs = []

        if first_log:
            self._logs.append(first_log)
