class English:
    def __init__(self):
        self.name = "English"

    def hello_english(self):
        return "Hello"


class Vietnamese:
    def __init__(self):
        self.name = "Vietnamese"

    def hello_vietnamese(self):
        return "Xin chaos"


class Adapter(English):
    def __init__(self, vn: Vietnamese):
        self.vn = vn

    def hello_english(self):
        return "Vietnamese says hello English"


vietnamese = Vietnamese()
translator = Adapter(vietnamese)
print(translator.hello_english())
