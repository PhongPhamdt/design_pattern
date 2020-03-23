from abc import abstractmethod


# Command
class Command:
    @abstractmethod
    def execute(self):
        pass


class LunchCommand(Command):
    def __init__(self, receiver_lunch):
        self.lunch = receiver_lunch

    def execute(self):
        self.lunch.make_lunch()


class DinnerCommand(Command):
    def __init__(self, receiver_dinner):
        self.dinner = receiver_dinner

    def execute(self):
        self.dinner.make_dinner()


# Listener
class Lunch:
    @staticmethod
    def make_lunch():
        print("Lunch is being made")


class Dinner:
    @staticmethod
    def make_dinner():
        print("Dinner is being made")


# Invoker
class MealInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


if __name__ == "__main__":
    lunch = Lunch()
    dinner = Dinner()
    command_lunch = LunchCommand(lunch)
    command_dinner = DinnerCommand(dinner)

    meal_invoker = MealInvoker(command_lunch)
    meal_invoker.invoke()

    meal_invoker.set_command(command_dinner)
    meal_invoker.invoke()
