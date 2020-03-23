class English:
    def __init__(self):
        self.name = "English"

    @staticmethod
    def hello_english():
        return "Hello"


class Vietnamese:
    def __init__(self):
        self.name = "Vietnamese"

    @staticmethod
    def hello_vietnamese():
        return "Xin chaos"


class Adapter(English):
    def __init__(self, vn: Vietnamese):
        super().__init__()
        self.vn = vn

    def hello_english(self):
        return "Vietnamese says hello English"


vietnamese = Vietnamese()
translator = Adapter(vietnamese)
print(translator.hello_english())
