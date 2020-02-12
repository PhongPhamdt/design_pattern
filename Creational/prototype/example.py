from copy import deepcopy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class Robot:
    def __str__(self):
        return "I am a Robot"


def main():
    a = Robot()
    prototype = Prototype()
    prototype.register('robot', a)
    b = prototype.clone('robot', acc="Bob")
    print(a)
    print(b, b.acc)


if __name__ == "__main__":
    main()
