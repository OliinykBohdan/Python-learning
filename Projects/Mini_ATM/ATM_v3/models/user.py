class User:
    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin
