'''
Create class - Budget
Each object should have a name
Be able to deposit, withdraw, and transfer between budgets
'''
class Budget():
    def __init__(self, name, amount=0.00):
        self.name = name
        self.amount = amount
        self.ledger = []

    def __repr__(self):
        return f'The budget for {self.name} is {self.amount}'

    def deposit(self, value, desc=''):
        self.amount += value
        self.ledger.append({'Amount':value, 'Description':desc})
        exec(f'with open("{self.name}.txt", "w") as file1: file1.write(str({self.amount}))')
        return value

    def withdraw(self, value, desc=''):
        self.amount -= value
        self.ledger.append({'Amount':-value, 'Description':desc})
        exec(f'with open("{self.name}.txt", "w") as file1: file1.write(str({self.amount}))')
        return value

    def transfer(self, budg, val):
        self.withdraw(val, f'Transfer to {budg.name}')
        budg.deposit(val, f'Transfer from {self.name}')
        exec(f'with open("{self.name}.txt", "w") as file1: file1.write(str({self.amount}))')
        exec(f'with open("{budg.name}.txt", "w") as file1: file1.write(str({budg.amount}))')
        return self.amount, budg.amount

    def history(self):
        print(f'{self.name} budget')
        for i in self.ledger:
            print(f'{i["Amount"]} \t {i["Description"]}')
        return f'Amount: {self.amount}'
        
    