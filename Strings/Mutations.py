list1=[]

def mutate_string(string, position, character):
    
    list1 =list(string)
    list1[position]=character
    str=''.join(list1)


    return str

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
