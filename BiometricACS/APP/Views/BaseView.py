from PyQt5.QtGui import QIcon, QPixmap


class BaseView:

    @staticmethod
    def setup_window_icon(QWidget):
        icon = QIcon()
        icon.addPixmap(QPixmap(".\APP\Sources\Icons\Program.ico"), QIcon.Normal, QIcon.Off)
        QWidget.setWindowIcon(icon)