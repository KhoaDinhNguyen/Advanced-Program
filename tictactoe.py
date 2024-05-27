import random
    
def printBoard(board):
    print("    a   b   c   d ")
    print("  +---------------+")
    for i in range(0,4):
        if board[i][0] == 0:
            print(str(i + 1) + " |  ", end = " ")
        elif board[i][0] == 1:
            print(str(i + 1) + " | X", end = " ")
        else:
            print(str(i + 1) + " | O", end = " ")
            
        for j in range(1,4):
            if board[i][j] == 0:
                print("|  ", end = " ")
            elif board[i][j] == 1:
                print("| X", end = " ")
            else:
                print("| O", end = " ")
        print("|")
        print("  +---------------+")
    
def chooseCell():
    cell = input("Enter the cell (example a1): ")
    return cell

def validateInput(cell):
    if len(cell) != 2:
        return False
    if not('a' <= cell[0] and cell[0] <= 'd'):
        return False
    if not('1' <= cell[1] and cell[1] <= '4'):
        return False
    return True
        
def mapCell(cell):
    return  (ord(cell[1]) - ord('1'), ord(cell[0]) - ord('a'))

def validateMove(board, pos):
    if(board[pos[0]][pos[1]] == 0):
        return True
    return False

def updateBoard(board, pos, player, winCondition):
    row = pos[0]
    col = pos[1]
    board[row][col] = player
    winCondition[player - 1][row] += 1
    winCondition[player - 1][col + 4] += 1
    if (row == col):
        winCondition[player - 1][8] += 1
    if(row + col == 3):
        winCondition[player - 1][9] += 1
        
def isWin(player, winCondition):
    for item in winCondition[player - 1]:
        if item ==  4:
            return True
    return False
    
def isTie(winCondition):
    tie = True
    for i in range(0, 10):
        tie = tie & (winCondition[0][i] != 0 and winCondition[1][i] != 0)
    return tie

def nextPlayer(player):
    if player == 1:
        return 2
    else:
        return 1
################################ 2 Players ###################################
def multiplayer(board, player, winCondition):
    printBoard(board)
    print("Player " + str(player) + " is playing...")
    
    cell = chooseCell()
    if not validateInput(cell):
        print("\nERROR: invalid move\n")
        return multiplayer(board, player, winCondition)
    
    pos = mapCell(cell)
    if not validateMove(board, pos):
        print("\nERROR: the cell was chosen\n")
        return multiplayer(board, player, winCondition)
    
    updateBoard(board, pos, player, winCondition)
    
    if isWin(player, winCondition):
        print("\nPlayer " + str(player) + " win!!!")
        printBoard(board)
        return
    if isTie(winCondition):
        print("The game is tie, no player win!!!")
        printBoard(board)
        return
    return multiplayer(board, nextPlayer(player), winCondition)

def multiplayerMode():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    winCondition = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    multiplayer(board, 1, winCondition)

################################ 1 Player ###################################

def computerMove(board, winCondition):
    pos = (random.randint(0, 3), random.randint(0, 3))
    if not validateMove(board, pos):
        return computerMove(board, winCondition)
        
    updateBoard(board, pos, 2, winCondition)
    
    if isWin(2, winCondition):
        print("\nComputer wins. You lose!!!")
        printBoard(board)
        return True
    if isTie(winCondition):
        print("The game is tie, you can not win!!!")
        printBoard(board)
        return True

    return False
    
def playFirst(board, winCondition):
    printBoard(board)
    
    print("Player is playing ...")
    
    cell = chooseCell()
    if not validateInput(cell):
        print("\nERROR: invalid move\n")
        return playFirst(board, winCondition)
    
    pos = mapCell(cell)
    if not validateMove(board, pos):
        print("\nERROR: the cell was chosen\n")
        return playFirst(board, winCondition)
    
    updateBoard(board, pos, 1, winCondition)
    
    if isWin(1, winCondition):
        print("\nPlayer wins!!!")
        printBoard(board)
        return
    if isTie(winCondition):
        print("The game is tie, no player win!!!")
        printBoard(board)
        return
    
    if computerMove(board, winCondition):
        return
    
    return playFirst(board, winCondition)

def playSecond(board, winCondition):
    if computerMove(board, winCondition):
        return

    return playFirst(board, winCondition)

def computerMode():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    winCondition = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    print("Play first or second?")
    
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