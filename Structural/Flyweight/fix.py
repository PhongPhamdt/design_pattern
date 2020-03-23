class Shape:
    def draw(self):
        pass


class ShapeFactory:
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, color, x, y):
        if color not in self.__instances:
            self.__instances[color] = Circle(color, x, y)
        return self.__instances[color]


class Circle(Shape):
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def draw(self):
        print("{} Circle {}-{}".format(self.__color, self.__x, self.__y))


if __name__ == "__main__":
    circle = ShapeFactory().get_instance("black",1,1)
    circle.draw()