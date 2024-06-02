import math

a = int(input('enter coefficient of x^2 : '))
b = int(input('enter coefficient of x : '))
c = int(input('enter coefficient of constant : '))

r1 =  complex(-b+math.sqrt(b**2-(4*a*c))/(2*a))
r2 =  complex(-b-math.sqrt(b**2-(4*a*c))/(2*a))

print('roots of given quadratic equation are : ',a,b)

