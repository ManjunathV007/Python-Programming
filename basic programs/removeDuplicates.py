list_l1 = [int(x) for x in input('enter elements into the list : ').split()]
list_l2 = []
for x in list_l1:
    if x not in list_l2:
        list_l2.append(x)

print(list_l2)
