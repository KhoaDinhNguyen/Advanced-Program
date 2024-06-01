import random # used for random move for computer

#==================================== BASIC FUNCTIONS ==========================================#

# printBoard() prints the board play
# board: the play board
def printBoard(board):
    print("    a   b   c   d ")
    print("  +---------------+")
    for i in range(0,4):
        print(str(i + 1), end = " ")
        for j in range(0,4):
            if board[i][j] == 0:
                print("|  ", end = " ")
            elif board[i][j] == 1:
                print("| X", end = " ")
            else:
                print("| O", end = " ")
        print("|")
        print("  +---------------+")

# chooseCell() takes the input from player
def chooseCell():
    return input("Enter the cell (example a1): ")

# validateInput() returns True if the input is valid
# cell: the input from chooseCell()
def validateInput(cell):
    if len(cell) != 2:
        return False
    if not('a' <= cell[0] and cell[0] <= 'd'):
        return False
    if not('1' <= cell[1] and cell[1] <= '4'):
        return False
    return True

# mapCell() return the tuple of row and column from the player input
# cell: the input from chooseCell()
def mapCell(cell):
    return  (ord(cell[1]) - ord('1'), ord(cell[0]) - ord('a'))

# validateMove() return True if the position does not occupied
# board: the play board
# pos: the position after mapCell()
def validateMove(board, pos):
    if(board[pos[0]][pos[1]] == 0):
        return True
    return False

# updateBoard() updates the board play and win game condition
# board: the play board
# pos: the position after mapCell()
# player: the current player
# winCondition: the win game condition matrix
def updateBoard(board, pos, player, winCondition):
    (row, col) = pos
    board[row][col] = player
    winCondition[player - 1][row] += 1
    winCondition[player - 1][col + 4] += 1
    if (row == col):
        winCondition[player - 1][8] += 1
    if(row + col == 3):
        winCondition[player - 1][9] += 1

# isWin() returns True if player wins game
# player: the current player
# winCondition: the win game condition matrix
def isWin(player, winCondition):
    return any([i == 4 for i in winCondition[player - 1]])

# isTie() returns True if the game is tie
# winCondition: the win game condition matrix
def isTie(winCondition):
    return all([winCondition[0][i] != 0 and winCondition[1][i] != 0 for i in range(0, 10)])

# nextPlayer() returns the next player of the current player
# player: the current player
def nextPlayer(player):
    if player == 1:
        return 2
    else:
        return 1

#==================================== MULTIPLAYER MODE ==========================================#
# multiplayer() execute the multiplayer mode
# board: the board play
# player: the current player
# winCondition: the win game condition matrix
def multiplayer(board, player, winCondition):
    # print board at first
    printBoard(board)
    print("Player " + str(player) + " is playing...")
    
    # take input from player and validate it
    # the player continue input until the input is valid
    cell = chooseCell()
    if not validateInput(cell):
        print("\nERROR: invalid move\n")
        return multiplayer(board, player, winCondition)
    
    pos = mapCell(cell)
    if not validateMove(board, pos):
        print("\nERROR: the cell was chosen\n")
        return multiplayer(board, player, winCondition)
    
    # the input is valid, update board
    updateBoard(board, pos, player, winCondition)
    
    # check the condition of winning game or the game is tie
    if isWin(player, winCondition):
        print("\nPlayer " + str(player) + " win!!!")
        printBoard(board)
        return
    if isTie(winCondition):
        print("\nThe game is tie, no player win!!!")
        printBoard(board)
        return
    
    # move to the next player
    return multiplayer(board, nextPlayer(player), winCondition)

# multiplayerMode() initializes the board play and winCondition matrix
def multiplayerMode():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    winCondition = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    multiplayer(board, 1, winCondition)

#==================================== COMPUTER MODE ==========================================#
# In Computer Mode, the computer always has value 2 in board play
# computerMove() 
# - randomly chooses position for computer to mark,
# - updates the board 
# - returns True if the game is tie or win. Otherwise, it returns false.
# board: the board play
# winCondition: the win game condition matrix
def computerMove(board, winCondition):
    # randomly choose a position until the position is valid
    pos = (random.randint(0, 3), random.randint(0, 3))
    if not validateMove(board, pos):
        return computerMove(board, winCondition)
    
    # update the board
    updateBoard(board, pos, 2, winCondition)
    
    # check win and tie condition
    if isWin(2, winCondition):
        print("\nComputer wins. You lose!!!")
        printBoard(board)
        return True
    if isTie(winCondition):
        print("The game is tie, you can not win!!!")
        printBoard(board)
        return True

    return False

# playFirst(): user play first
# board: the board play
# winCondition: the win game condition matrix
def playFirst(board, winCondition):
    # print board at first
    printBoard(board)
    print("Player is playing ...")
    
    # take input from player and validate it
    # the player continue input until the input is valid
    cell = chooseCell()
    if not validateInput(cell):
        print("\nERROR: invalid move\n")
        return playFirst(board, winCondition)
    
    pos = mapCell(cell)
    if not validateMove(board, pos):
        print("\nERROR: the cell was chosen\n")
        return playFirst(board, winCondition)
    
    # the input is valid, update board
    updateBoard(board, pos, 1, winCondition)
    
    # check the condition of winning game or the game is tie
    if isWin(1, winCondition):
        print("\nPlayer wins!!!")
        printBoard(board)
        return
    if isTie(winCondition):
        print("\nThe game is tie, no player win!!!")
        printBoard(board)
        return
    
    # if computerMove return True then the game is end
    if computerMove(board, winCondition):
        return
    
    # continue play game
    return playFirst(board, winCondition)

# playSecond() actually just makes computer move first then we run playFirst() again.
# board: the board play
# winCondition: the win game condition matrix
def playSecond(board, winCondition):
    if computerMove(board, winCondition):
        return

    return playFirst(board, winCondition)

# computerMode() initializes the board play and winCondition matrix
def computerMode():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    winCondition = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    print("Play first or second?")
    
    # ask option for playing first and second
    turn = askOption("Type 1 for First and 2 for Second: ", "Invalid order", "1", "2")       
    if turn == "1":    
        playFirst(board, winCondition)
    else:
        playSecond(board, winCondition)
    
def askOption(prompt, invalidPrompt, option1, option2):
    choose = input(prompt)
    
    if choose != option1 and choose != option2:
        return twoOption(invalidPrompt, option1, option2)

    return choose
    
def twoOption(prompt, option1, option2):
    print(prompt)
    choose = input("Choose again: ")
    if choose != option1 and choose != option2:
        return twoOption(prompt, option1, option2)

    return choose

#==================================== EXTENSION ==========================================#
def tictactoe():
    print("\nGAME START!!!\n")
    
    print("Choose 2 versions to play game: Computer and Multiplayer?")
    
    version = askOption("Type M for Multiplayer and C for Computer: ", "Invalid version of play game", "M", "C")

    if version == "M":
        print("MUTIPLAYER\n")
        multiplayerMode()    
    else:
        print("\nPLAY WITH COMPUTER!!\n")
        computerMode()
        
    print("\nGAME END !!!\n")

def intro():
    print("This program is a demo of TIC-TAC-TOE GAME !!!\n")
    print("Tic-tac-toe is a game in which players take turns marking the spaces in a 3 x 3 grid with X or O.")
    print("The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.\n")
    print("However, in this program, we initialize the game with 4 x 4 grid making the game has more space to choose\n")

def playAgain():
    print("Do you want to play again or try different version?")      
    play = askOption("Type Y for YES and N for NO: ", "Invalid input", "Y", "N")
            
    if play == "Y":
        tictactoe()
        return playAgain()
        
    return

def main():
    print("---------------------- PROGRAM START !!! ----------------------\n")
    intro()
    print("Do you want to try this game?")
    
    play = askOption("Type Y for YES and N for NO: ", "Invalid input", "Y", "N")
        
    if play == "N":
        print("\n---------------------- PROGRAM END !!! ----------------------\n")
        return
    
    tictactoe()    
    playAgain()
    
    print("\n---------------------- PROGRAM END !!! ----------------------\n")
    
    return

#==================================== DEMO ==========================================#
multiplayerMode()