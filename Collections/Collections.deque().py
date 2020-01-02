# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d= deque()
no_of_operations= int(input())

for _ in range(no_of_operations):
    entry = input().split()
    if entry[0]=='append':
        d.append(entry[1])
    elif entry[0]=='appendleft':
        d.appendleft(entry[1])
    elif entry[0]=='pop':
        d.pop()
    elif entry[0]=='popleft':
        d.popleft()
print(*d)
