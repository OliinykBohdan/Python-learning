from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} by card')


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} via PayPal')


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} in crypto')


def process_payment(payment: Payment):
    payment.pay(100)


process_payment(CardPayment())
process_payment(PayPalPayment())
process_payment(CryptoPayment())
