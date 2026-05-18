class Account:
    def __init__(self, balance):
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            return 'Withdraw amount must be less than or equal to balance.'

        if withdraw_amount <= 0:
            return 'Withdraw amount must be greater than or equal to 0.'

        self.__balance -= withdraw_amount
        self.__history.append(f'Withdraw: {withdraw_amount}')

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            return 'Deposit amount must be greater than or equal to 0.'

        self.__balance += deposit_amount
        self.__history.append(f'Deposit: {deposit_amount}')
