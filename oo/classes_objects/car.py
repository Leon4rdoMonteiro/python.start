class Car:

    # Class attributes 
    # No depends of class instance
    x = 'Abcd'


    # Constructor method
    def __init__(self, name, maker, year, color):
        # Object attributes
        self.name = name
        self.maker = maker
        self.year = year
        self.color = color


    # Instance method
    def drive(self):
        print(self. name + ' created')


    # Static method
    # Has no access to class attributes/methods 
    # No depends of class instance
    @staticmethod
    def hello():
        print('Hello World!')


    # Class method
    # Has no access to instance methods/attributes
    # No depends of class instance
    @classmethod
    def get(cls):
        print(cls.x)