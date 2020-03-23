class State:
    def alert(self, context):
        pass


class Vibration(State):
    def alert(self, context):
        print("The phone is {}".format(self))

    def __str__(self):
        return "Vibration"


class Ringing(State):
    def alert(self, context):
        print("The phone is {}".format(self))

    def __str__(self):
        return "Ringing"


class Silent(State):
    def alert(self, context):
        print("The phone is {}".format(self))

    def __str__(self):
        return "Silent ..."


class Context:
    __state = None

    def __init__(self):
        self.__state = Ringing()

    def set_state(self, state: State):
        self.__state = state

    def alert(self):
        self.__state.alert(self)


if __name__ == "__main__":
    phone = Context()
    ring = Ringing()
    silent = Silent()
    vibrate = Vibration()
    phone.alert()
    phone.set_state(silent)
    phone.alert()
    phone.set_state(vibrate)
    phone.alert()
