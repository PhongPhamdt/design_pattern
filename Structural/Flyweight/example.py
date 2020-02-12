class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class SpamFactory(object):
    def  __init__(self):
        self.__instances = dict()

    def get_instance(self, a, b):
        if (a, b) not in self.__instances:
            self.__instances[(a, b)] = Spam(a, b)
        return self.__instances[(a, b)]


class Egg(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class EggFactory(object):
    def __init__(self):
        self.__instances = dict()
    def get_instance(self, x, y):
        if (x, y) not in self.__instances:
            self.__instances[(x, y)] = Egg(x, y)
        return self.__instances[(x, y)]


spamFactory = SpamFactory()
eggFactory = EggFactory()

print(spamFactory.get_instance(1, 2))
print(spamFactory.get_instance(1, 2))
print(eggFactory.get_instance('a', 'b'))
print(eggFactory.get_instance('a', 'b'))
print(spamFactory.get_instance(1, 2))
print(eggFactory.get_instance(1, 2))
