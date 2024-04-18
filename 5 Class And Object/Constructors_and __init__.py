class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

my_phone = Phone('Foco f4', 'Redmi', 420000)
print(my_phone.name, my_phone.brand, my_phone.price)