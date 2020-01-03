# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n = int(input())
s = map(int , input().split())

least_common= Counter(s).most_common()[-1][0]
print(least_common)
