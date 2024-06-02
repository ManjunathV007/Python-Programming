#Dummy class
class negativeAgeException(Exception):
    pass

def stage(age):
    if age<0:
        raise negativeAgeException('Invalid age- Age should not be Negative!')
    elif 0<=age<13:
        print('you are a Kid')
    elif 13<=age<=19:
        print('you are a Teen')
    elif 20<=age<=50:
        print('you are a YoungPerson')
    else:
        print('you are a oldPerson')

try:
 age = int(input('enter age : '))
 stage(age)
except negativeAgeException as e:
    print(e)

