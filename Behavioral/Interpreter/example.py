class Expression:
    def interpreter(self, con):
        pass


class TerminalExpression(Expression):
    def __init__(self, data):
        self._data = data

    def interpreter(self, con):
        if self._data in con:
            return True
        else:
            return False


class OrExpression(Expression):
    def __init__(self, ex1: Expression, ex2: Expression):
        self._ex1 = ex1
        self._ex2 = ex2

    def interpreter(self, con):
        return self._ex1.interpreter(con) or self._ex2.interpreter(con)


class AndExpression(Expression):
    def __init__(self, ex1: Expression, ex2: Expression):
        self._ex1 = ex1
        self._ex2 = ex2

    def interpreter(self, con):
        return self._ex1.interpreter(con) and self._ex2.interpreter(con)


def main():
    person1 = TerminalExpression("Alice")
    person2 = TerminalExpression("Bob")
    single = OrExpression(person1, person2)
    twin = AndExpression(person1, person2)
    print(single.interpreter("Bob"))
    print(single.interpreter("Cathy"))
    print(twin.interpreter("Bob n Alice"))
    print(twin.interpreter("Bob n Cathy"))


if __name__ == "__main__":
    main()
