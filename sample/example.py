class X:
    def call(self):
        print("X")


class Y:
    def call(self):
        print("Y")


class Z:
    def call(self):
        print("Z")


class T:
    def call(self):
        print("T")


class A(X,Y):
    def load(self):
        print("A")


class B(Z,T):
    def load(self):
        print("B")


class M(A,B): pass


m = M()
m.call()
m.load()
