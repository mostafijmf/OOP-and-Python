class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    
    def remove_item(self, index):
        self.cart.pop(index)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']

        print('total price',total)
        if amount < total:
            print(f'Please provide {total - amount} tk')
        else:
            print(f'Here is your return tk {amount - total}')


my_shopping = Shopping('my_shopping')
my_shopping.add_to_cart('laptop', 500, 3)
my_shopping.add_to_cart('mobile', 100, 5)
my_shopping.checkout(1000)
my_shopping.remove_item(0)
my_shopping.checkout(1000)