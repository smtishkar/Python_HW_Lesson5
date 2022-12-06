# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота

from random import randint



sweets = 117
player1 = 'Игрок № 1'
player2 = 'Игрок № 2'
bot = 'Бот'
count = 1               #Переключатель кто ходит
max = 28

participant = int(input("Введите цифру с кем хотите играть (1) - человек или (2) - бот: "))

if participant == 1:
    print (f'У нас всего {sweets} конфет ')
    print (f'Ходит {player1}')

    while sweets > 0:
        if count == 1:
            take = int(input("Введите количество конфет которое хотите взять: "))
            while take > max + 1:
                print("Максимальное количество конфет, которое можно взять = 28")
                take = int(input("Введите количество конфет которое хотите взять: "))                  
            if take <sweets and take < max+1 : 
                sweets = sweets - take
                print (f'Осталось {sweets} конфет ')
                count = 2
                print (f'Ходит {player2}')
            elif take > sweets:
                while take > sweets:
                    print(f"У нас осталось всего {sweets} конфет")
                    take = int(input("Введите количество конфет которое хотите взять: "))                
                if take < sweets and sweets !=0:
                    sweets = sweets - take
                    print (f'Осталось {sweets} конфет ')
                    count = 2
                    print (f'Ходит {player2}')
                else:    
                    print(f"{player1} победил")
                    print('Игра окончена')
                    break                
            elif take == sweets and take < max+1:
                print(f"{player1} победил")
                print('Игра окончена')
                break
        elif count == 2:
            take = int(input("Введите количество конфет которое хотите взять: "))
            while take > max + 1:
                print("Максимальное количество конфет, которое можно взять = 28")
                take = int(input("Введите количество конфет которое хотите взять: "))                  
            if take <sweets and take < max+1 : 
                sweets = sweets - take
                print (f'Осталось {sweets} конфет ')
                count = 1
                print (f'Ходит {player1}')
            elif take > sweets:
                while take > sweets:
                    print(f"У нас осталось всего {sweets} конфет")
                    take = int(input("Введите количество конфет которое хотите взять: "))                
                if take < sweets and sweets !=0:
                    sweets = sweets - take
                    print (f'Осталось {sweets} конфет ')
                    count = 1
                    print (f'Ходит {player1}')
                else:    
                    print(f"{player1} победил")
                    print('Игра окончена')
                    break                
            elif take == sweets and take < max+1:
                print(f"{player2} победил")
                print('Игра окончена')
                break

if participant == 2:
    print (f'У нас всего {sweets} конфет ')
    print (f'Ходит {player1}')

    while sweets > 0:
        if count == 1:
            take = int(input("Введите количество конфет которое хотите взять: "))
            while take > max + 1:
                print("Максимальное количество конфет, которое можно взять = 28")
                take = int(input("Введите количество конфет которое хотите взять: "))                  
            if take <sweets and take < max+1 : 
                sweets = sweets - take
                print (f'Осталось {sweets} конфет ')
                count = 2
                print (f'Ходит {bot}')
            elif take > sweets:
                while take > sweets:
                    print(f"У нас осталось всего {sweets} конфет")
                    take = int(input("Введите количество конфет которое хотите взять: "))                
                if take < sweets and sweets !=0:
                    sweets = sweets - take
                    print (f'Осталось {sweets} конфет ')
                    count = 2
                    print (f'Ходит {bot}')
                else:    
                    print(f"{player1} победил")
                    print('Игра окончена')
                    break                
            elif take == sweets and take < max+1:
                print(f"{player1} победил")
                print('Игра окончена')
                break
        elif count == 2:
            take = randint(1,28)
            print (f"{bot} взял {take} конфет")             
            if take <sweets and take < max+1 : 
                sweets = sweets - take
                print (f'Осталось {sweets} конфет ')
                count = 1
                print (f'Ходит {player1}')
            elif take > sweets:
                while take > sweets:
                    print(f"У нас осталось всего {sweets} конфет")
                    take = take = randint(1,sweets)
                    print (f"{bot} взял {take} конфет")                
                if take < sweets and sweets !=0:
                    sweets = sweets - take
                    print (f'Осталось {sweets} конфет ')
                    count = 1
                    print (f'Ходит {player1}')
                else:    
                    print(f"{bot} победил")
                    print('Игра окончена')
                    break                
            elif take == sweets and take < max+1:
                print(f"{bot} победил")
                print('Игра окончена')
                break










#             # 1. Создайте программу для игры с конфетами человек против человека.
# # *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# # a) Добавьте игру против бота





# sweets = 117
# player1 = 'Игрок № 1'
# player2 = 'Игрок № 2'
# count = 1               #Переключатель кто ходит
# max = 28

# print (f'У нас всего {sweets} конфет ')
# print (f'Ходит {player1}')

# while sweets > 0:
#     if count == 1:
#         take = int(input("Введите количество конфет которое хотите взять: "))
#         while take > max + 1:
#             print("Максимальное количество конфет, которое можно взять = 28")
#             take = int(input("Введите количество конфет которое хотите взять: "))                  
#         if take <sweets and take < max+1 : 
#             sweets = sweets - take
#             print (f'Осталось {sweets} конфет ')
#             count = 2
#             print (f'Ходит {player2}')
#         elif take > sweets:
#             while take > sweets:
#                 print(f"У нас осталось всего {sweets} конфет")
#                 take = int(input("Введите количество конфет которое хотите взять: "))                
#             if take < sweets and sweets !=0:
#                 sweets = sweets - take
#                 print (f'Осталось {sweets} конфет ')
#                 count = 2
#                 print (f'Ходит {player2}')
#             else:    
#                 print(f"{player1} победил")
#                 print('Игра окончена')
#                 break                
#         elif take == sweets and take < max+1:
#             print(f"{player1} победил")
#             print('Игра окончена')
#             break
#         # else:
#         #     print(f"Максимальное количество конфет, которое можно взять = 28")
#     elif count == 2:
#         take = int(input("Введите количество конфет которое хотите взять: "))
#         if take <sweets and take < max+1 : 
#             sweets = sweets - take
#             print (f'Осталось {sweets} конфет ')
#             count = 2
#             print (f'Ходит {player2}')
#         elif take > sweets:
#             while take > sweets:
#                 print(f"У нас осталось всего {sweets} конфет")
#                 take = int(input("Введите количество конфет которое хотите взять: "))                
#             if take < sweets and sweets !=0:
#                 sweets = sweets - take
#                 print (f'Осталось {sweets} конфет ')
#                 count = 2
#                 print (f'Ходит {player2}')
#             else:    
#                 print(f"{player1} победил")
#                 print('Игра окончена')
#                 break                
#         elif take == sweets and take < max+1:
#             print(f"{player1} победил")
#             print('Игра окончена')
#             break
#         else:
#             print(f"Максимальное количество конфет, которое можно взять = 28")