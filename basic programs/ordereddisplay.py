n = 1

while n<=5:
 s = input('enter item name : ')
 price = input('enter price : ')
 total_len = len(s)+len(price)
 dots = '.' * (30 - total_len)
 print(s + dots + price)
 n = n+1
