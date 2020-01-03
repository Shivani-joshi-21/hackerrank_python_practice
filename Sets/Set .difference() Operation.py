# Enter your code here. Read input from STDIN. Print output to STDOUT
m= int(input())
set_m= set(map(int,input().split()))
n= int(input())
set_n=set(map(int, input().split()))
print(len(set_m.difference(set_n)))
