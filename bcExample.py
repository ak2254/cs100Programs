import bankaccount
import random

account = bankaccount.BankAccount(10, 50, 'John Smith')
fCount = 0
for i in range(100):
    choice = random.randint(0,1)
    ammount = random.randint(1, 20)
    if choice == 1:
        account.deposit(ammount)
    elif choice ==0:
        withdrawFlag = account.withdraw(ammount)
        if withdrawFlag == False:
            fCount +=1
print("fail count ", fCount)
print("Balance ", account.getBalance())
    
    
    
