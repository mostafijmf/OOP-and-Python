class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money


    # The @property is a built-in decorator for the property() function in Python. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.

    # -- getter without any setter is readonly attribute --
    @property
    def age(self):
        return self._age
    
    # -- getter --
    @property
    def salary(self):
        return self.__money
    
    # -- setter --
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'Salary can not be negative'
        self.__money += value
    

dev = User('Mostafij', 23, 5000)
# print(dev.age())
print(dev.age)
print(dev.salary)
dev.salary = 10000
print(dev.salary)