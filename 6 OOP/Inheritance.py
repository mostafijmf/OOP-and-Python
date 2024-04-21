# Common Attributes
class Common:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def run(self):
        return f'Running: {self.brand}'


class Laptop(Common):
    def __init__(self, brand, price, color, memory):
        self.memory = memory
        super().__init__(brand, price, color)
    
    def coding(self):
        return f'Learning Python'
    
    def __repr__(self):
        return f'Brand: {self.brand}, Price: {self.price}, Color: {self.color}, Memory: {self.memory}'
    
class Phone(Common):
    def __init__(self, brand, price, color, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color)
        
    def phone_call(self, number, text):
        return f'Sending sms to: {number} whit: {text}'
    
    def __repr__(self):
        return f'Brand: {self.brand}, Price: {self.price}, Color: {self.color}, Dual Sim: {self.dual_sim}'
    
iphone = Phone('Iphone 15', 150000, 'Black', True)
laptop = Laptop('Asus', 100000, 'Black', '1TB')

print(iphone)
print(laptop)