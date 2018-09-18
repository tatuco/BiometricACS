from BiometricACS.View.LoginPanelView import LoginPanenView


class LoginPanelController():

    def __init__(self, model):
        self.model = model
        self.mView = LoginPanenView(self.model, self)
        self.mView.show()