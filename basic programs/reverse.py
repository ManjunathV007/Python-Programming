n = int(input('enter a number :  '))
rev = 0
m = n

while n>0:
    r = n%10
    n = n//10
    rev = rev * 10 + r
print(rev)

if m == rev:
    print('palindrome')
else:
    print('not palindrome')
