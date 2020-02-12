from abc import ABC, abstractmethod


class IceCream(ABC):

    @property
    def need_spoon(self):
        return False

    def __str__(self):
        string = self.__class__.__name__
        for key, value in self.__dict__.items():
            string += "\n{}: {}".format(key, value)
        string += "\n"
        return string


class ConeIceCream(IceCream):
    pass


class CupIceCream(IceCream):

    @property
    def need_spoon(self):
        return True


class Builder(ABC):

    @abstractmethod
    def __init__(self):
        self.product = None
        self.toppings = None

    def set_flavors(self, flavors):
        self.product.flavors = flavors
        return self

    def set_toppings(self):
        if self.toppings is not None:
            self.product.toppings = self.toppings
        return self

    def add_spoon(self):
        if self.product.need_spoon:
            self.product.spoon = 1
        return self

    def get_product(self):
        return self.product


class ConeIceCreamBuilder(Builder):

    def __init__(self):
        super().__init__()
        self.product = ConeIceCream()
        self.toppings = "hazelnuts"


class CupIceCreamBuilder(Builder):

    def __init__(self):
        super().__init__()
        self.product = CupIceCream()
        self.toppings = "chocolate chips"


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def build_product(self, flavors):
        return (
            self.builder.set_flavors(flavors).set_toppings().add_spoon().get_product()
        )


# Client: it creates a Director object and configures it with a Builder object.


def main():
    director = Director(ConeIceCreamBuilder())
    product = director.build_product(["chocolate", "vanilla", "banana"])
    print(product)

    director = Director(CupIceCreamBuilder())
    product = director.build_product(["lemon", "strawberry"])
    print(product)

    builder = ConeIceCreamBuilder()
    director = Director(builder)
    builder.toppings = None  # the ConeIceCreamBuilder has no more toppings!
    product = director.build_product(["chocolate", "vanilla", "banana"])
    print(product)


if __name__ == "__main__":
    main()
