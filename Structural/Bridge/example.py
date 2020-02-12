class PayoutService:
#     amount = 0
    def __init__(self, gateway, amount):
        self.gateway = gateway
        self.amount = amount

    def pay(self):
        self.gateway.paid(self.amount)

    def pay_with_bonus(self, bonus):
        self.gateway.paid(self.price*(1 -bonus))

    def price(self):
        return self.amount


class Invoice(PayoutService):
#     vat = 0
    def __init__(self, gateway, amount, vat):
        self.gateway = gateway
        self.amount = amount
        self.vat = vat
        print("Invoice\n")

    def price(self):
        return self.amount + self.vat


class Receipt(PayoutService):
    def __init__(self, gateway, amount):
        self.gateway = gateway
        self.amount = amount
        print("Receipt\n")

    def pay_half(self):
        return self.pay_with_bonus(0.5)


class PaymentGateway:
    def paid(self, amount):
        pass


class PayPal(PaymentGateway):
    def paid(self, amount):
        print("paid {} by PayPal".format(amount))


class TransferWise(PaymentGateway):
    def paid(self, amount):
        print("paid {} by TransferWise".format(amount))


# Client code
payment = Invoice(TransferWise(), 1000, 10)
payment.pay()
