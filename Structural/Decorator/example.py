class TextTag:
    """Represents a base text tag"""
    def render(self):
        pass


class Html(TextTag):
    """html text"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class Decorator(TextTag):
    _text = None

    def __init__(self, text):
        self._text = text

    def render(self):
        self._text.render()


class BoldWrapper(Decorator):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(Decorator):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = Html("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())
