from PyQt5.QtWidgets import QMainWindow, QWidget
from .WindowLoginPanel import  Ui_wLoginPanel

class LoginPanenView(QWidget, Ui_wLoginPanel):

    def __init__(self, model, controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(wLoginPanel=self)
