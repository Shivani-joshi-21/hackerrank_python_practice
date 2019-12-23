def minion_game(string):
    # your code goes here

    
    VOWELS = "AEIOU"

    length = len(string)
    stuart_score = 0
    kevin_score = 0
    for x in range(length):
        if string[x] not in VOWELS:  # ==> For Staurt's score
            stuart_score += length - x
        else:  # ==> For Kevin's
            kevin_score += length - x

   
    if stuart_score > kevin_score:
        print('Stuart '+str(stuart_score))
    elif stuart_score<kevin_score:
        print('Kevin '+str(kevin_score))
    else:
        print("Draw")
   
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
