import abc


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def check_temperature(self, temp):
        pass


class HikeStrategy(Strategy):
    def check_temperature(self, temp):
        if 50 <= temp <= 90:
            return True
        else:
            return False


class SkiStrategy(Strategy):
    def check_temperature(self, temp):
        if temp <= 32:
            return True
        else:
            return False


class Context:
    def __init__(self, temp, strategy: Strategy):
        self.temperature = temp
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_temperature(self):
        return self.temperature

    def get_result(self):
        return self.strategy.check_temperature(self.temperature)


if __name__ == '__main__':
    temperature = 60

    strategy_ski = SkiStrategy()
    context = Context(temperature, strategy_ski)

    print("Is the temperature ({} F) good for skiing? {}".format(context.get_temperature(), context.get_result()))

    strategy_hike = HikeStrategy()
    context.set_strategy(strategy_hike)

    print("Is the temperature ({} F) good for hiking? {}".format(context.get_temperature(), context.get_result()))
