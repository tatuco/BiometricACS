from PyQt5.QtWidgets import QWidget
from BiometricACS.Utility.Observer import Observer
from .WindowLoginPanel import Ui_wLoginPanel


class LoginPanenView(QWidget, Observer):
    def __init__(self, imModel, inController, parent=None):
        super(QWidget, self).__init__(parent)
        self.mController = inController
        self.mModel = imModel
        self.mModel.addObserver(self)

        self.ui = Ui_wLoginPanel()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.mController.loginClicked)
        self.ui.btnCancel.clicked.connect(self.mController.cancelClicked)

    def modelIsChanged(self):
        if self.mModel.isRegistredUser():
            #TODO Open sub windows
            self.destroy(destroySubWindows=False)
