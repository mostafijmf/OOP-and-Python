balance = 3000
def buy(item, price):
    global balance
    balance = balance - price
    print(f'balance after buying {item}', balance)

buy('mobile', 2000)
print(balance)