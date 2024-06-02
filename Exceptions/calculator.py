def add(a, b):
    print('addition result - ', a + b)


def mult(a, b):
    print('Multiplication result - ', a * b)


def div(a, b):
    if b == 0:
        raise ZeroDivisionError('Invalid number,Divide by 0')
    print('Division result - ', a / b)


def sub(a, b):
    print('Subtraction result - ', a - b)


print('*******************Calculator***********************')
a = int(input('enter number -a : '))
b = int(input('enter number - b : '))
print('1.Addition')
print('2.Subtraction')
print('3.Division')
print('4.Multiplication')
choice = int(input('enter your choice : '))
try:
    match choice:
        case 1:
            add(a, b)
        case 2:
            sub(a, b)
        case 3:
            div(a, b)
        case 4:
            mult(a, b)
except ZeroDivisionError as e:
    print(e)

