# Enter your code here. Read input from STDIN. Print output to STDOUT

subjects,student = map(int,input().strip().split())

marks=[]

for i in range (student):
    marks.append(map(float , input().split()))
    
for j in zip(*marks):
    print(sum(j)/student)
