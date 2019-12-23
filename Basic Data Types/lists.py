list1 = []
n = int(raw_input())
for i in range(n):
    a = raw_input().split()
    command = a[0]
    if command == 'append':
        list1.append(int(a[1]))
    elif command == 'print':
        print(list1)
    elif command == 'insert':
        list1.insert(int(a[1]), int(a[2]))
    elif command == 'reverse':
        list1 = list1[::-1]
    elif command == 'pop':
        list1.pop()
    elif command == 'sort':
        list1 = sorted(list1)
    elif command == 'remove':
        list1.remove(int(a[1]))
