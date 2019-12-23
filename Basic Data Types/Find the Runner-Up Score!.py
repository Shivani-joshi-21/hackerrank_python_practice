if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    l1=set(arr)
    l1.remove(max(arr))
    print(max(l1))
