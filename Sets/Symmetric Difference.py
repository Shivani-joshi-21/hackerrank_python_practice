# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
set_m = set(map(int, input().split()))
n = input()
set_n = set(map(int, input().split()))

x=set_m.symmetric_difference(set_n)
for i in sorted(x):
    print(i , end="\n")
