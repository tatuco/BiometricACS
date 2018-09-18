class LoginPanelModel():

    def __init__(self, ):
        self._mUsername = ''
        self._mPassword = ''
        self._user = []

        self._mObservers = []

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if value==[self._mUsername, self._mPassword]:
            return
        self._mUsername = value[0]
        self._mPassword = value[1]
        self.notifyObservers()

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self):
        for o in self._mObservers:
            o.modelIsChanged()

    def isRegistredUser(self):
        # TODO sql querry to db return true or false
        # userstatus = sql.execute()

        # base realization...
        user_status = self._mUsername == 'postgres' and self._mPassword == '123'
        print('Login status: %s'%user_status)
        return user_status
