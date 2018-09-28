from BiometricACS.APP.View.LoginPanelView import LoginPanenView
from PyQt5 import QtCore


class LoginPanelController():

    def __init__(self, imModel):
        self.mModel = imModel
        self.mView = LoginPanenView(self.mModel, self)
        self.mView.show()

    def entetrClicled(self, event):
        if event.key() + 1 == QtCore.Qt.Key_Enter:
            self.loginClicked()

    def loginClicked(self):
        username = self.mView.ui.tbUsername.text()
        password = self.mView.ui.tbPassword.text()
        self.mModel.update(username, password, None)

    def cancelClicked(self):
        exit(0)

    def isRegistredUser(self):
        db = DataContext()
        user = db.session.query(type(self.mModel)).filter_by(type(self.mModel).username==self.mView.ui.tbUsername.text() and type(self.mMode).password==self.mView.ui.tbPassword.text()).first()
        print(user)
        if user!=None:
            print('asff')
        return user!=None
