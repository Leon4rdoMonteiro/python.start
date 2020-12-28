class Car:

    # Class attributes
    x = 'Abcd'

    # Constructot method
    def __init__(self, name, maker, year, color):
        # Object attributes
        self.name = name
        self.maker = maker
        self.year = year
        self.color = color


    def drive(self):
        print(self. name + ' created')