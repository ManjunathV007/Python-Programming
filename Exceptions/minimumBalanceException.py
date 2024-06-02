class minimumBalanceException(Exception):
    pass

def withdraw(amount,balance):
    minBalance = 1000
    balance = balance - amount
    if balance<minBalance:
        raise minimumBalanceException('Cannot withdraw amount - Minimum Balance is not maintained')
    else:
        print('Amount has been successfully withdrawn : ',amount,',available balance : ', balance)


balance = int(input('Enter balance : '))
amount = int(input('Enter amount to Withdraw : '))
try:
    withdraw(amount,balance)
except minimumBalanceException as e:
    print(e)