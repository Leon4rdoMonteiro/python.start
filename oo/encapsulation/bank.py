class Account:

    def __init__(self, number):
        self.number = number
        self.total = 0

    
    def deposit(self, value):
        self.total += value

    def withdraw(self, value):
        self.total -= value

    def get_total(self):
        return self.total