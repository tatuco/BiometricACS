from PyQt5.QtWidgets import QWidget
from BiometricACS.BLL.Utility import Observer
from BiometricACS.APP.UI.WindowLoginPanel import Ui_wLoginPanel


class LoginPanenView(QWidget, Observer):
    def __init__(self, inModel, inController, parent=None):
        super(QWidget, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel
        self.mModel.addObserver(self)

        self.ui = Ui_wLoginPanel()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.mController.loginClicked)
        self.ui.btnCancel.clicked.connect(self.mController.cancelClicked)

    def keyPressEvent(self, QKeyEvent):
        self.mController.entetrClicled(QKeyEvent)

    def modelIsChanged(self):
        if self.mController.isRegistredUser():
            #TODO Open sub windows
            self.destroy(destroySubWindows=False)
