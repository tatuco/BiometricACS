import enum
from PyQt5.QtCore import Qt


class LogLevels(enum.Enum):
    INFO = Qt.black
    ACCESS = Qt.darkGreen
    WARNING = Qt.red
