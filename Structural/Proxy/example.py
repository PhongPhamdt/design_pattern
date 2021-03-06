import time


class SalesManager:
    def talk(self):
        pass


class RealSalesManager(SalesManager):
    def talk(self):
        print("Sales Manager ready to talk")


class Proxy(SalesManager):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = RealSalesManager()
            time.sleep(1)
            self.sales.talk()
        else:
            time.sleep(1)
            print("Sales Manager is busy")


class NoTalkProxy(SalesManager):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(1)
        print("This Sales Manager will not talk to you", "whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
