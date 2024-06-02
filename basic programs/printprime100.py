
print('prime numbers are : ')
for i in range(1,101):
    count = 0
    for j in range(1, 100 + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print(i)


