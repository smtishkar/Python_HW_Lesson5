# 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)



def print_area():
    print (' '*30)
    print (area[0],' | ', area[1],' | ', area[2])
    print('-'*2,'+','-'*3,'+', '-'*2)
    print (area[3],' | ', area[4],' | ', area[5])
    print('-'*2,'+','-'*3,'+', '-'*2)
    print (area[6],' | ', area[7],' | ', area[8])

def step_area(step,symbol):
    area[step-1] = symbol

def winner ():
    win = ''
    for i in victory_matrix:
        if area [i[0]] == "X"  and area[i[1]] == "X" and area[i[2]] == "X":
            win = 'X'
        if area [i[0]] == "O"  and area[i[1]] == "O" and area[i[2]] == "O":
            win = 'O'
    return win

victory_matrix = [[0, 1, 2],
[3, 4, 5],
[6, 7, 8],
[0, 3, 6],
[1, 4, 7],
[2, 5, 8],
[0, 4, 8],
[2, 4, 6]]

def print_sep (sep, sep_len):
    print(sep * sep_len)


area = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1               # Переключатель игрока   
player1 = "Игрок № 1"
player2 = "Игрок № 2"
game_over = 0           #Переключатель продолжения игры

print_sep(' ',30)
print (f"Ходит {player1}")
print_sep('-',30)
print_area()
while game_over == 0:
    if count == 1:
        symbol = "X"
        step = int(input("Введите цифру где хотите разместить символ: "))
        step_area(step,symbol)
        winner()
        print_area()
        if winner() == 'X':
            game_over = 1
            print ("Игра окончена. Победил 'X'")
            break
        count = 2
        print_sep('-',30)
        print (f"Ходит {player2}")
        print_sep(' ',30)

    elif count == 2:
        symbol = "O"
        step = int(input("Введите цифру где хотите разместить символ: "))
        step_area(step,symbol)
        winner()
        print_area()
        if winner() == 'X':
            game_over = 1
            print ("Игра окончена. Победил 'O'")
            break
        count = 1
        print_sep('-',30)
        print (f"Ходит {player1}")
        print_sep(' ',30)
