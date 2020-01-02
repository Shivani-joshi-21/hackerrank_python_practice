# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

no_of_shoes = int(input())
sizes_in_stock=collections.Counter(map(int, input().split()))
no_of_cust= int(input())
earnings=0

for i in range(no_of_cust):
    size,price = map(int ,input().split())
    if(sizes_in_stock[size]):
        earnings+=price
        sizes_in_stock[size]-=1
print (earnings)
    
