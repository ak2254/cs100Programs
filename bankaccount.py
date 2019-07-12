class BankAccount:
    def __init__(self, balance, accNumber,customerName):
        self.Balance = balance
        self.accNum = accNumber
        self.cName = customerName
    def deposit(self,amount):
        self.Balance +=amount
    def withdraw(self, amount):
        if self.Balance >= amount:
            self.Balance = self.Balance - amount
            return True
        else:
            return False
    def getBalance(self):
        return self.Balance
