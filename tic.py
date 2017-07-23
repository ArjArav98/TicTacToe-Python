"""
This program is meant to simulate a working model of Tic-Tac-Toe in Python
Author:- Arjun Aravind
Date Started:- 22.7.2017
Python:- Version 3.6.1
Refer documentation for more details on functions and related code
"""

"""
Function Declaration starts here
"""

def printVerticalSpace():
    for i in range(0,10):
        print("\n\n\n\n")

def printRules(rules):
    for i in range(0,4):
        length=len(rules[i])
        a=""
        count=0
        for j in range(0,length):
            if ((count>=42) or (j==(length-1))):
                print(a)
                a="    "
                count=4
            a+=rules[i][j]
            count+=1

def printBoard(board):
    print("\n")
    for i in range(0,2):
        print("{:^42}".format("     |     |     "))
        print("{:^42}".format("  {b1}  |  {b2}  |  {b3}  ".format(b1=board[i][0], b2=board[i][1], b3=board[i][2])))
        print("{:^42}".format("_____|_____|_____"))
    print("{:^42}".format("     |     |     "))
    print("{:^42}".format("  {b1}  |  {b2}  |  {b3}  ".format(b1=board[2][0], b2=board[2][1], b3=board[2][2])))
    print("{:^42}".format("     |     |     "))
    print("\n")

def boardRowCheck(boardRow):
    if boardRow[0]!=" " and boardRow[1]!=" " and boardRow[2]!=" ":
        return 1
    else:
        return 0

def gameEndCheck(board, playerShapes):
    
    for i in range(0,3):
        if (board[i][0]==board[i][1] and board[i][1]==board[i][2] and boardRowCheck(board[i])):
            print("Player {player} wins!\n".format(player=playerShapes.index(board[i][0])+1))
            return 1
    
    for i in range(0,3):
        if (board[0][i]==board[1][i] and board[1][i]==board[2][i] and boardRowCheck([board[0][i], board[1][i], board[2][i]])):
            print("Player {player} wins!\n".format(player=playerShapes.index(board[0][i])+1))
            return 1
    
    if  (board[0][0]==board[1][1] and board[1][1]==board[2][2] and boardRowCheck([board[0][0], board[1][1], board[2][2]])):
            print("Player {player} wins!\n".format(player=playerShapes.index(board[1][1])+1))
            return 1
    
    elif (board[2][0]==board[1][1] and board[1][1]==board[0][2] and boardRowCheck([board[2][0], board[1][1], board[0][2]])):
            print("Player {player} wins!\n".format(player=playerShapes.index(board[1][1])+1))
            return 1
            
    return 0

def positionEmpty(board, row, col):
    if board[row][col]=="X" or board[row][col]=="O":
        return 0
    else: 
        return 1

def positionValid(pos):
    if pos>=1 and pos<=9:
        return 1
    else:
        return 0

def boardInput(pos, board, charac):
    pos-=1
    row=(int(pos/3))
    col=(pos%3)
    
    board[row][col]=charac
    return board

"""
Function Declaration ends here
"""

#CodeSegment1

printVerticalSpace()

print("==========================================")
print("{:*^42}".format(" TIC-TAC-TOE "))
print("==========================================")

print("\n")

print("{:^42}".format("============"))
print("{:^42}".format("RULES"))
print("{:^42}".format("============"))

print("")

rules=[]
rules.append("--> The game can be played by a maximum of two players.")
rules.append("--> The two players will have to play with either an X or an O.")
rules.append("--> The positions in the game range from 1 to 9. ")
rules.append("--> At every turn, the players will have to enter the position and press ENTER.")

printRules(rules)

#CodeSegment2A

player=1
playerShape=["X", "O"]
errorMessage=False
gameCount=1
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
startOption=int(input("\n\n\nWould you like to start the game? Press any button to start and 0 to exit.\n--> "))

#CodeSegment2B

while startOption!=0 and gameCount<=9:
    
    if player==1:
        player=0
    elif player==0:
        player=1
    
    #CodeSegment2B1
    
    printVerticalSpace()
    printBoard(board)
    
    print("\nIt is now the turn of Player {player} ({playerShape})".format(player=player+1, playerShape=playerShape[player]))
    if errorMessage:
        print("Make sure you enter a valid position.")
        print("Make sure you enter a position which is empty.")
    
    pos=int(input("Player {player}, enter your position (from 1 to 9) --> ".format(player=player+1)))
    
    #CodeSegment2B2
    
    if positionEmpty(board, (int((pos-1)/3)), ((pos-1)%3)) and positionValid(pos):
        gameCount+=1
        board=boardInput(pos, board, playerShape[player])
        printVerticalSpace()
        printBoard(board)
        if gameEndCheck(board, playerShape):
            startOption=0
    else:
        errorMessage=True
        player=1-player

#CodeSegment3

print("Thanks for playing!\n")