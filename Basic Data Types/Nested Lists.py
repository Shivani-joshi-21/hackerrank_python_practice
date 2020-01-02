if __name__ == '__main__':
        marksheet=[]
        scorelist=[]
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=list(set(scorelist))
        b.sort()
        second_highest =b[1]
        for name,score in sorted(marksheet):
            if score==second_highest:
                 print(name)
       
