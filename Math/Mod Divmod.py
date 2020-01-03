# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
n1,n2= int(input()),int(input())
a = divmod(n1,n2)
print(a[0])
print(a[1])
print(a)
