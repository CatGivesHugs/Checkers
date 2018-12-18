top = ['\t    a   b   c   d   e   f   g   h   \n']
row8 = ['\t8  ', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '\n\t  --------------------------------\n']
row7 = ['\t7  ', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '\n\t  --------------------------------\n']
row6 = ['\t6  ', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '|', ' ', '|', 'B', '\n\t  --------------------------------\n']
row5 = ['\t5  ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '\n\t  --------------------------------\n']
row4 = ['\t4  ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '\n\t  --------------------------------\n']
row3 = ['\t3  ', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '\n\t  --------------------------------\n']
row2 = ['\t2  ', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '\n\t  --------------------------------\n']
row1 = ['\t1  ', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '|', 'W', '|', ' ', '\n\n']
board = [top, row8, row7, row6, row5, row4, row3, row2, row1]
for i in board:
    for pos in i:
        print(pos, end=' ')
turn = 0
rCount = 12
bCount = 12
player = input('Which piece would you like to move? (a3, c3 etc...) ')
while rCount != 0 and bCount != 0:
    if turn % 2 == 0:
        if player == 'a3' and row3[1] == 'W':
            pSpot = input(' Where would you like to move this spot? ')
            while pSpot != 'b4' and row4[3] != 'W':
                pSpot = input('Invalid option. Choose another spot to move this piece. ')
            if pSpot == 'b4' and row4[3] == ' ':
                del(row3[1])
                row3.insert(1, ' ')
                del(row4[3])
                row4.insert(3, 'W')
            elif pSpot == 'b4' and row5[3] == 'B':
                del(row3[1])
                row3.insert(1, ' ')
                del(row4[3])
                del(row5[5])
                row5.insert(5, 'W')
        elif player == 'c3' and row3[5] == 'W':
            pSpot = input(' Where would you like to move this spot? ')
            while pSpot != 'b4' and (pSpot == 'b4' and row4[3] == 'W') and pSpot != 'd4' and (pSpot == 'd4' and row4[7] == 'W'):
                pSpot = input('Invalid option. Choose another spot to move this piece. ')
            if pSpot == 'b4' and row4[3] == ' ':
                del(row3[5])
                row3.insert(5, ' ')
                del(row4[3])
                row4.insert(3, 'W')
            elif pSpot == 'b4' and row4[3] == 'B':
                del(row3[5])
                row3.insert(5, ' ')
                del(row4[3])
                row4.insert(3, ' ')
                del(row5[1])
                row5.insert(1, 'W')
            elif pSpot == 'd4' and row4[7] == ' ':
                del(row3[5])
                row3.insert(5, ' ')
                del(row4[7])
                row4.insert(7, 'W')
            elif pSpot == 'd4' and row4[7] == 'B':
                del(row3[5])
                row3.insert(5, ' ')
                del(row4[7])
                row4.insert(7, ' ')
                del(row5[9])
                row5.insert(9, 'W')
        elif player == 'e3' and row3[5] == 'W':
            pSpot = input(' Where would you like to move this spot? ')
            if pSpot == 'd4' and row4[3] == ' ':
                del(row3[9])
                row3.insert(9, ' ')
                del(row4[7])
                row4.insert(7, 'W')
            elif pSpot == 'd4' and row4[3] == 'B':
                del(row3[9])
                row3.insert(9, ' ')
                del(row4[7])
                row4.insert(7, ' ')
                del(row5[5])
                row5.insert(5, 'W')
            elif pSpot == 'f4' and row4[7] == ' ':
                del(row3[9])
                row3.insert(9, ' ')
                del(row4[11])
                row4.insert(11, 'W')
            elif pSpot == 'f4' and row4[7] == 'B':
                del(row3[9])
                row3.insert(9, ' ')
                del(row4[11])
                row4.insert(11, ' ')
                del(row5[13])
                row5.insert(13, 'W')
        elif player == 'g3' and row3[5] == 'W':
            pSpot = input(' Where would you like to move this spot? ')
            # Add a while loop that detects if h4 is black
            if pSpot == 'f4' and row4[3] == ' ':
                del(row3[13])
                row3.insert(13, ' ')
                del(row4[11])
                row4.insert(11, 'W')
            elif pSpot == 'f4' and row4[3] == 'B':
                del(row3[13])
                row3.insert(13, ' ')
                del(row4[11])
                row4.insert(11, ' ')
                del(row5[9])
                row5.insert(9, 'W')
            elif pSpot == 'h4' and row4[7] == ' ':
                del(row3[13])
                row3.insert(13, ' ')
                del(row4[15])
                row4.insert(15, 'W')

    if turn % 2 != 0:
        if player == 'b6' and row6[3] == 'B':
            pSpot = input(' Where would you like to move this spot? ')
            while pSpot != 'c5' and (pSpot == 'c5' and row5[5] == 'B') and pSpot != 'a5' and (pSpot == 'a5' and row5[1] =='B'):
                pSpot = input('Invalid option. Choose another spot to move this piece. ')
            if pSpot == 'c5' and row5[3] == ' ':
                del(row6[3])
                row6.insert(3, ' ')
                del(row5[5])
                row5.insert(5, 'B')
            elif pSpot == 'c5' and row5[3] == 'W':
                del(row6[1])
                row6.insert(3, ' ')
                del(row5[5])
                row5.insert(5, ' ')
                del(row4[7])
                row4.insert(7, 'B')
            elif pSpot == 'a5' and row5[1] == ' ':
                del(row6[3])
                row6.insert(3, ' ')
                del(row5[1])
                row5.insert(1, 'B')

    for i in board:
        for pos in i:
            print(pos, end=' ')
    player = input('Which piece would you like to move? ')
    turn += 1
if rCount == 0:
    print('Player 2 wins!')
elif bCount == 0:
    print('Player 1 wins!')
