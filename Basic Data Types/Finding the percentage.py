if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score1 = student_marks[query_name]
    avg = sum(score1)/len(score1)
    print("%.2f"%avg)
    