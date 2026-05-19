class User:
    def __init__(self, username, pin, account):
        self.username = username
        self.__pin = pin
        self.account = account

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin
