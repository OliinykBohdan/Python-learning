class Payment:
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} by card')


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} in crypto')


payments = [CardPayment(), CryptoPayment()]

for p in payments:
    p.pay(100)
