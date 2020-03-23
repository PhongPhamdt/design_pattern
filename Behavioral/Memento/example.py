class Memento:
    def restore(self):
        pass


class Originator:
    def save(self):
        pass


class ConcreteOriginator:
    def __init__(self, state):
        self.__state = state

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def save(self):
        return ConcreteMemento(self, self.__state)


class ConcreteMemento(Memento):
    def __init__(self, originator: ConcreteOriginator, state):
        self.__originator = originator
        self.__state = state

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def restore(self):
        self.__originator.set_state(self.__state)


class CareTaker:
    __history = []

    def __init__(self, memento: Memento):
        self.__history.append(memento)

    def undo(self):
        if self.__history is not None:
            self.__history.pop().restore()


if __name__ == "__main__":
    ori = ConcreteOriginator("ONE")
    mem = ConcreteMemento(ori, ori.get_state())
    caretaker = CareTaker(mem)
    print(ori.get_state())
    ori.set_state("TWO")
    print(ori.get_state())
    caretaker.undo()
    print(ori.get_state())
