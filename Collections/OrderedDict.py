# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n= int(input())
o = OrderedDict()
for i in range(n):
    item =input().split()
    name= ' '.join(item[:-1])
    price= int(item[-1])

    if name in o:
        o[name]+=price
    else:
        o[name] = price

for name,price in o.items():
    print(name,price)
