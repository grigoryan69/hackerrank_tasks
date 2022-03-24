def minion_game(value):
    kevin = 0
    student = 0
    # English vowels in lower and upper cases  
    vow="AaEeIiOoUu"
    for i in range(len(value)):
        if value[i] in vow:
            kevin = kevin + len(value) -i
        else:
            student = student + len(value) -i    
    
    if kevin > student:
        print(f'Kevin {kevin}')
       
    elif student > kevin:
        print(f'Stuart {student}') 

    else:
        print("Draw")           


if __name__ == '__main__':
    s = input()
    minion_game(s)
