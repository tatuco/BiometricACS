from PyQt5.QtWidgets import QWidget
from . import MainView
from ..Utilities import Observer
from ..UI import Ui_wLoginPanel
from ..AppStart import program_logs


class LoginPanelView(QWidget, Observer):
    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.controller = in_controller
        self.model = in_model
        self.model.add_observer(self)

        self.ui = Ui_wLoginPanel()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.controller.login_clicked)
        self.ui.btnCancel.clicked.connect(self.controller.cancel_clicked)

    def keyPressEvent(self, QKeyEvent):
        self.controller.enter_clicked(QKeyEvent)

    def model_is_changed(self):
        self.controller.main()
