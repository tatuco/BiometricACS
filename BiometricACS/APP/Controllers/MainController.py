from ..Views import MainView, ReloginPanelView
from ..Controllers.ReloginPanelController import ReloginPanelController
from ...BLL.DTO import AccountDTO, AccountRoleDTO, ChekpointDTO, VisitDTO, CamerasVectorDTO, EmployeeStatusDTO, CameraDTO


class MainController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.view = MainView(in_model, self, parent)

        self.user_changed()

        self.view.show()

    def _update_ui_role(self, is_technical_engineer):
        self.view.ui.menuData.setEnabled(is_technical_engineer)
        self.view.ui.menuSettings.setEnabled(is_technical_engineer)
        self.view.ui.actionCreateAccount.setEnabled(is_technical_engineer)
        self.view.ui.actionExport_Accounts.setEnabled(is_technical_engineer)

    def user_changed(self):
        if self.model.relogin_service.user.role == AccountRoleDTO.viewer:
            self._update_ui_role(False)
        elif self.model.relogin_service.user.role == AccountRoleDTO.technical_engineer:
            self._update_ui_role(True)
        else:
            print('relogin fatal error')

    def relogin_clicked(self):
        relogin_controller = ReloginPanelController(self.model.relogin_service, self.view)

    def cancel_clicked(self):
        self.view_close()

    def view_close(self):
        self.view.close()
