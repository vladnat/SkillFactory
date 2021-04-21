table = list(range(1,10))

def draw_table(table):
    print ("-" * 13)
    for i in range(3):
        print ("|", table[0+i*3], "|", table[1+i*3], "|", table[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = int(input(f"Выберите клеточку для {player_token}: "))
            
        if 1 <= player_answer <= 9:
        
            if (str(table[player_answer-1]) not in "XO"):
                table[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Выберите другую клеточку.")

def check_win(table):
    win_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_combination:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False

def play(table):
    counter = 0
    win = False
    while not win:
        draw_table(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(table)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_table(table)

play(table)