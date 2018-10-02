from PyQt5.QtWidgets import QWidget
from ..Utilities import Observer
from ..UI import Ui_wLoginPanel
from ..AppStart import program_logs, Log, datetime


class LoginPanelView(QWidget, Observer):
    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.mController = in_controller
        self.mModel = in_model
        self.mModel.add_observer(self)

        self.ui = Ui_wLoginPanel()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.mController.login_clicked)
        self.ui.btnCancel.clicked.connect(self.mController.cancel_clicked)

    def keyPressEvent(self, QKeyEvent):
        self.mController.entetr_clicled(QKeyEvent)

    def model_is_changed(self):
        result, user = self.mController.is_registred()
        print(result)
        if result:
            # TODO Open sub windows
            program_logs.add_log(Log(datetime.now(), 'Login as %s'% user.username))
            print(program_logs.logs)
            self.destroy(destroySubWindows=False)
