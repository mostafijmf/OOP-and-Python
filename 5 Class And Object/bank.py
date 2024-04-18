class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100        
        self.max_withdraw = 100000

    def get_balance(self):
        print(self.balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You can not withdraw less than {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')


ibbl = Bank(100000)
ibbl.deposit(5000)
ibbl.get_balance()
ibbl.withdraw(999)
ibbl.get_balance()