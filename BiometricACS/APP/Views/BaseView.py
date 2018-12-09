from PyQt5.QtGui import QIcon, QPixmap


class BaseView:

    @staticmethod
    def setup_window_icon(widget):
        icon = QIcon()
        icon.addPixmap(QPixmap(".\APP\Sources\Icons\Program.ico"), QIcon.Normal, QIcon.Off)
        widget.setWindowIcon(icon)