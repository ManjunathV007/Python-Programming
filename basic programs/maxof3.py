def findmax(a,b,c):
    if a>b :
        if a > c:
            print('a is greater')
        else:
            print('c is greater')
    if b>a :
        if b > c:
            print('b is greater')
        else:
            print('c is greater')

findmax(10,5,2)
findmax(5,10,2)
findmax(5,2,10)
