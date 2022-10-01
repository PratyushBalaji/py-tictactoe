board = [] # game board itself as a 2d array
game = True # while loop condition that toggles based on game = play or end
winCondition = [[0,0,2,2,4,4],[0,4,2,2,4,0],[0,0,2,0,4,0],[0,2,2,2,4,2],[0,4,2,4,4,4],[0,0,0,2,0,4],[2,0,2,2,2,4],[4,0,4,2,4,4]] 
# 2d arrays are the best, i can make smaller arrays of each of the 8 possible win conditions and compare them on board itself!!
debug = True
turn = 'x'

def checkWin():# function to check win condition
    global board, game
    for i in winCondition:# using list of possible win scenarios
        if game == True:
            if board[i[0]][i[1]] == board[i[2]][i[3]] == board[i[4]][i[5]] and board[i[0]][i[1]] != " ":
                game = False
                if debug:print(f"Win Coordinates : {i[0]},{i[1]} {i[2]},{i[3]} {i[4]},{i[5]}")
                print(f"{board[i[0]][i[1]]} has won the game!")

def checkDraw():
    global game
    temp = 0
    if game == True:
        for i in board:
            for j in i:
                if j != ' ':
                    temp+=1
        if temp == 25:
            game = False
            print("The game has ended in a tie")

def setupBoard():# function to set up the board to neutral state
    global board
    # rows
    board = [" ",' | '," ",' | '," "]
    board = [board*5 for _ in range(5)]

    # spacers
    board[1] = ["-"," + ","-"," + ","-"]
    board[3] = ["-"," + ","-"," + ","-"]

    # correction
    board[0] = board[0][:5]
    board[2] = board[2][:5]
    board[4] = board[4][:5]
    
    if debug:print(f"Setup Board : ");printBoard()

def printBoard():# function to display the board at any time
    global board
    string = ""
    for i in board:
        string = ""
        for j in i:
            string+=j
        print(string)

setupBoard()
while game == True:# runs while the game is not won or drawn
    print(f"\nTurn : {turn}")
    arg = input("Move : ")
    move = arg
    try:
        if "," in list(move):
            coords = move.split(',')
            if debug:print(f"coords : {coords}")
        else:
            print(board[6][6])
        try:
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
            if board[(coords[1]*2) - 2][(coords[0]*2) - 2] == " ":
                board[(coords[1]*2) - 2][(coords[0]*2) - 2] = turn
                if turn == 'x':turn = 'o'
                elif turn == 'o':turn = 'x'
                printBoard()
            else:
                print(f"Invalid Space : {coords[0]},{coords[1]} is already filled")        
        except:
            print('Invalid Coordinates : Values must be between 1 and 3 (inclusive)')
    except:
        print('Invalid Move : Please provide coordinates')
    checkWin()
    checkDraw()

"""
What I can do : 
1̶)̶ ̶M̶a̶k̶e̶ ̶i̶t̶ ̶s̶o̶ ̶y̶o̶u̶ ̶c̶a̶n̶'̶t̶ ̶o̶v̶e̶r̶w̶r̶i̶t̶e̶ ̶a̶ ̶t̶i̶l̶e̶ ̶t̶h̶a̶t̶ ̶a̶l̶r̶e̶a̶d̶y̶ ̶h̶a̶s̶ ̶a̶ ̶v̶a̶l̶u̶e̶ ̶(̶C̶h̶e̶c̶k̶ ̶i̶f̶ ̶t̶h̶e̶ ̶l̶o̶c̶a̶t̶i̶o̶n̶ ̶=̶=̶ ̶'̶ ̶'̶ ̶a̶n̶d̶ ̶i̶f̶ ̶s̶o̶,̶ ̶c̶h̶a̶n̶g̶e̶,̶ ̶e̶l̶s̶e̶ ̶p̶r̶i̶n̶t̶ ̶'̶i̶n̶v̶a̶l̶i̶d̶ ̶s̶p̶o̶t̶'̶)̶
̶#̶ ̶ ̶ ̶ ̶ ̶a̶)̶ ̶M̶a̶k̶e̶ ̶a̶n̶ ̶a̶r̶r̶a̶y̶ ̶w̶i̶t̶h̶ ̶a̶l̶l̶ ̶p̶o̶s̶s̶i̶b̶l̶e̶ ̶s̶p̶o̶t̶s̶ ̶(̶0̶,̶0̶ ̶t̶o̶ ̶2̶,̶2̶)̶ ̶a̶n̶d̶ ̶r̶e̶m̶o̶v̶e̶ ̶s̶p̶o̶t̶s̶ ̶a̶s̶ ̶t̶h̶e̶y̶ ̶a̶r̶e̶ ̶u̶s̶e̶d̶,̶ ̶t̶h̶e̶n̶ ̶w̶h̶e̶n̶ ̶i̶n̶v̶a̶l̶i̶d̶,̶ ̶p̶r̶i̶n̶t̶ ̶o̶u̶t̶ ̶a̶l̶l̶ ̶v̶a̶l̶i̶d̶ ̶s̶p̶o̶t̶s̶
2̶)̶ ̶M̶a̶k̶e̶ ̶i̶t̶ ̶a̶l̶t̶e̶r̶n̶a̶t̶e̶ ̶b̶e̶t̶w̶e̶e̶n̶ ̶x̶'̶s̶ ̶a̶n̶d̶ ̶o̶'̶s̶ ̶s̶o̶ ̶i̶t̶ ̶i̶s̶ ̶r̶e̶a̶l̶l̶y̶ ̶l̶i̶k̶e̶ ̶t̶i̶c̶ ̶t̶a̶c̶ ̶t̶o̶e̶ ̶a̶n̶d̶ ̶n̶o̶t̶ ̶a̶l̶l̶o̶w̶ ̶a̶n̶y̶ ̶r̶a̶n̶d̶o̶m̶ ̶c̶h̶a̶r̶a̶c̶t̶e̶r̶s̶ ̶t̶o̶ ̶b̶e̶ ̶u̶s̶e̶d̶
3̵)̵ ̵A̵d̵d̵ ̵d̵e̵b̵u̵g̵ ̵v̵a̵r̵ ̵&̵ ̵m̵a̵k̵e̵ ̵1̵ ̵l̵i̵n̵e̵ ̵i̵f̵ ̵s̵t̵a̵t̵m̵e̵n̵t̵s̵ ̵(̵i̵f̵ ̵d̵e̵b̵u̵g̵:̵p̵r̵i̵n̵t̵(̵v̵a̵r̵i̵a̵b̵l̵e̵)̵)̵ ̵s̵o̵ ̵t̵h̵a̵t̵ ̵a̵n̵y̵t̵i̵m̵e̵ ̵a̵n̵y̵o̵n̵e̵ ̵w̵a̵n̵t̵s̵ ̵t̵o̵ ̵d̵e̵b̵u̵g̵,̵ ̵i̵t̵ ̵c̵a̵n̵ ̵b̵e̵ ̵d̵o̵n̵e̵ ̵w̵i̵t̵h̵ ̵1̵ ̵v̵a̵r̵ ̵b̵e̵i̵n̵g̵ ̵t̵o̵g̵g̵l̵e̵d̵̵

1 IS DONE!!
2 IS DONE!!
3 IS DONE!!

WANTED FUNCTIONALITY IS THERE, NOW WORK ON UI

New concepts used : 
1) 2d array. Makes life so much easier with accessing (no need of if statements for line1, line2, line3) and overwriting.
   Makes life so much easier for checking win condition (no need of writing individual if statements per win condition, an array of 6 numbers works)
   ↪ I think the implementation of the winCondition array is ingenious. 6 simple numbers to be read in pairs with 1 single if statement is awesome.
   ↪ Also allows for custom win patterns. Simply add new or delete existing win conditions
   ↪ This technique was inspired by the .json file used for minecraft recipes. Specifically the "pattern:[]" part of it
"""