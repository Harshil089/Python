from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Bank Transfer.")


class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()
    payment_context = PaymentContext(credit_card)

    payment_context.make_payment(100)  # Output: Paid 100 using Credit Card.
    payment_context.set_payment_strategy(paypal)

    payment_context.make_payment(50)  # Output: Paid 50 using PayPal.
    payment_context.set_payment_strategy(bank_transfer)
    payment_context.make_payment(200)  # Output: Paid 200 using Bank Transfer.
