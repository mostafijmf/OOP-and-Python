class Shop:
    shopping_mall = 'Jamuna'
    # cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mahi = Shop('mahi')
mahi.add_to_cart('shoe')
mahi.add_to_cart('phone')
print(mahi.buyer, mahi.cart)

irfan = Shop('irfan')
irfan.add_to_cart('hat')
irfan.add_to_cart('watch')
print(irfan.buyer, irfan.cart)

shuvo = Shop('shuvo')
shuvo.add_to_cart('chiruni')
print(shuvo.buyer, shuvo.cart)