class VoteHub:
    __vote = None
    product = 0

    @staticmethod
    def get_instance():
        """ Static access method. """
        if VoteHub.__vote is None:
            VoteHub()
        return VoteHub.__vote

    def __init__(self):
        """ Virtually private constructor. """
        if VoteHub.__vote is not None:
            raise Exception("This class is a singleton! Call get_instance() instead")
        else:
            VoteHub.__vote = self

    def add_vote(self):
        self.product += 1
        return self.product


x = VoteHub()
print(x)

y = VoteHub.get_instance()
print(y)

print(x.add_vote())  # 1
print(y.add_vote())  # 2
print(x.add_vote())  # 3
