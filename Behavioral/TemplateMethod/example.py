import abc


class Meal(metaclass=abc.ABCMeta):
    # template method
    def do_meal(self):
        self.prepare_ingredients()
        self.cook()
        self.eat()
        self.clean_up()

    def eat(self):
        print("Mmm, that's good")

    @abc.abstractmethod
    def prepare_ingredients(self):
        pass

    @abc.abstractmethod
    def cook(self):
        pass

    @abc.abstractmethod
    def clean_up(self):
        pass


class HamburgerMeal(Meal):
    def prepare_ingredients(self):
        print("Getting burgers, buns, and french fries")

    def cook(self):
        print("Cooking burgers on grill and fries in oven")

    def clean_up(self):
        print("Throwing away paper plates")


class TacoMeal(Meal):
    def prepare_ingredients(self):
        print("Getting ground beef and shells")

    def cook(self):
        print("Cooking ground beef in pan")

    def eat(self):
        print("The tacos are tasty")

    def clean_up(self):
        print("Doing the dishes")


class BaboMeal(Meal):
    def prepare_ingredients(self):
        print("Getting babo, milk, sugar, etc")

    def cook(self):
        print("Boil babo, put all together")

    def eat(self):
        print("This more like drink :))))")

    def clean_up(self):
        print("Throw away bottle :)))")


if __name__ == '__main__':
    meal1 = HamburgerMeal()
    meal1.do_meal()
    print("-----")

    meal2 = TacoMeal()
    meal2.do_meal()
    print("-----")

    meal2 = BaboMeal()
    meal2.do_meal()
    print("-----")
