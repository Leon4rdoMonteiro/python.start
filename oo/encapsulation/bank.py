class Bank1Account(object):

    # Cannot access attributes directly
    # Private attributes: add __ before attribute name
    def __init__(self, number):
        self.number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value
        self.__total -= 1

    def get_total(self):
        return self.__total


# Heritage
class Bank2Account(Bank1Account):
    # Used to use all inherited attributes/methods
    # pass

    # Overwrite constructor method
    def __init__(self, number, cvv):
        super(Bank2Account, self).__init__(number)
        self.cvv = cvv

    # Method overwrite
    def withdraw(self, value):
        self._Bank1Account__total -= value
        self._Bank1Account__total -= 2