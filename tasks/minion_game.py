def minion_game(string):
    kevin = 0
    student = 0
    # English vowels in lower and upper cases 
    vow="AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vow:
            kevin += len(string) -i
        else:
            student += len(string) -i    
    
    if kevin > student:
        print(f'Kevin {kevin}')
       
    elif student > kevin:
        print(f'Stuart {student}') 

    else:
        print("Draw")    

if __name__ == '__main__':
    s = input()
    minion_game(s)