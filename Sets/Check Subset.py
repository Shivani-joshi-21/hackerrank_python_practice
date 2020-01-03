# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a,b,c,d = input(), set(input().split()), input(), set(input().split())

    print(b.issubset(d))
