n=int(input())

s = set(map(int,input().split()))

commands=int(input())

for _ in range(commands) :

    entry=input().split()
    if entry[0]=="pop" :
        s.pop()
    elif entry[0]=="remove" :
        s.remove(int(entry[1]))
    elif entry[0]=="discard" :
        s.discard(int(entry[1]))
print (sum(s))
