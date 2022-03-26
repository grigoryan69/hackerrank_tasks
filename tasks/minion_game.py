def minion_game(string):
    kevin = 0
    student = 0
    # English vowels in lower and upper cases 
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            kevin += len(string) -i
        else:
            student += len(string) -i    
    
    winer = [kevin, student]
    if kevin == student:
        print("Draw")
    else:    
        print(f'Kevin {max(winer)}' if kevin > student \
        else f'Stuart {max(winer)}')

if __name__ == '__main__':
    s = input()
    minion_game(s)
