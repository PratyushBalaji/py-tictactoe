line1 = [' ',' | ',' ',' | ',' ']
line2 = [' ',' | ',' ',' | ',' ']
line3 = [' ',' | ',' ',' | ',' ']
spacer = '- + - + -'
game = True

# Function to print out the game board at any given moment
def printBoard():
    global spacer, line1, line2, line3
    for i in line1:
        print(i,end="")
    print()
    print(spacer)
    for i in line2:
        print(i,end="")
    
    print()
    print(spacer)
    for i in line3:
        print(i,end="")
    print()

def checkWin():
    global line1, line2, line3, game
    
    # Rows
    if line1[0] == line1[2] and line1[2] == line1[4] and line1[0] != ' ': # top row 
        if not line1[0] == 0:print(f"{line1[0]} has won the game!");game = False
    elif line2[0] == line2[2] and line2[2] == line2[4] and line2[0] != ' ': # mid row 
        if not line2[0] == 0:print(f"{line2[0]} has won the game!");game = False
    elif line3[0] == line3[2] and line3[2] == line3[4] and line3[0] != ' ': # bot row 
        if not line3[0] == 0:print(f"{line3[0]} has won the game!");game = False

    # Columns
    elif line1[0] == line2[0] and line2[0] == line3[0] and line1[0] != ' ': # l col
        if not line1[0] == 0:print(f"{line1[0]} has won the game!");game = False
    elif line1[2] == line2[2] and line2[2] == line3[2] and line1[2] != ' ': # mid col
        if not line1[1] == 0:print(f"{line1[1]} has won the game!");game = False
    elif line1[4] == line2[4] and line2[4] == line3[4] and line1[4] != ' ': # r col
        if not line1[2] == 0:print(f"{line1[2]} has won the game!");game = False

    # Diagonals
    elif line1[0] == line2[2] and line2[2] == line3[4] and line1[0] != ' ': # tlbr diag
        if not line1[0] == 0:print(f"{line1[0]} has won the game!");game = False
    elif line1[4] == line2[2] and line2[2] == line3[0] and line1[4] != ' ': # trbl diag
        if not line1[2] == 0:print(f"{line1[2]} has won the game!");game = False

print("Tic Tac Toe Game : \n Make a move by typing in the letter and the coordinates for where that letter should go! \n Example : 'x 0,0' ")
while game == True:
    # move at any given moment
    arg = input("Move : ")
    move = arg.split(' ')
    move[0] = move[0][:1]
    # mapping the input to the x and y coords (position on game board)
    try:
        coords = move[1].split(',')
        # print(coords)
        try:
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
            if coords[1] == 0:
                if coords[0] == 0:
                    line1[0] = move[0]
                elif coords[0] == 1:
                    line1[2] = move[0]
                elif coords[0] == 2:
                    line1[4] = move[0]
                else:x = line1[3]
            elif coords[1] == 1:
                if coords[0] == 0:
                    line2[0] = move[0]
                elif coords[0] == 1:
                    line2[2] = move[0]
                elif coords[0] == 2:
                    line2[4] = move[0]
                else:x = line2[3]
            elif coords[1] == 2:
                if coords[0] == 0:
                    line3[0] = move[0]
                elif coords[0] == 1:
                    line3[2] = move[0]
                elif coords[0] == 2:
                    line3[4] = move[0]
                else:x = line3[3]
            else:
                x = line1[3]
        except:
            print('Invalid Coordinates (from 0,0 to 2,2)')
    except:
        print('Invalid Move')


    # printing the board after every move
    printBoard()

    checkWin()

    if line1[0] != ' ' and line1[2] != ' ' and line1[4] != ' ' and line2[0] != ' ' and line2[2] != ' ' and line2[4] != ' ' and line3[0] != ' ' and line3[2] != ' ' and line3[4] != ' ' and game == True:
        print("No one won the game :(")
        game = False

"""

What I can do : 
1) Make it so you can't overwrite a tile that already has a value (Check if the location == ' ' and if so, change, else print 'invalid spot')
    a) Make an array with all possible spots (0,0 to 2,2) and remove spots as they are used, then when invalid, print out all valid spots
2) Make it alternate between x's and o's so it is really like tic tac toe and not allow any random characters to be used

"""