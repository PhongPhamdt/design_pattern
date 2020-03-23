class Subscriber:
    def update(self, state):
        pass


class Shop:
    __subscribers = []
    __main_state = None

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)
        else:
            print("{} is subscribing".format(subscriber))

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)
        else:
            print("{} is not subscribing".format(subscriber))

    def notify(self):
        for s in self.__subscribers:
            s.update(self.__main_state)

    def update_state(self, new_state):
        self.__main_state = new_state


class Customer(Subscriber):
    def __init__(self, name):
        self.__name = name

    def update(self, state):
        print("{} Received update {} from Shop".format(self.__name, state))


if __name__ == "__main__":
    publisher = Shop()
    c1 = Customer("Alice")
    c2 = Customer("Cathy")
    c3 = Customer("Bob")
    publisher.subscribe(c1)
    publisher.subscribe(c3)
    publisher.subscribe(c2)
    publisher.update_state("Iphone XII")
    publisher.notify()
    publisher.unsubscribe(c2)
    publisher.update_state("MAC BOOK PRO 2020")
    publisher.notify()
