def ValidateInput(integer):

    try:
        integer = int(integer)
        return integer, True
    except ValueError:
        print("You're a fucking low-life scumbag! Do you not know how to use a fucking keyboard? Friggin Idiot!", "\n")
        return integer, False


def GetPlayerName():

    Player1 = input("Enter Player 1 name:")
    Player2 = input("Enter Player 2 name:")
    return Player1, Player2


def PrintPlayerName(Player1, Player2):

    print(Player1)
    print(Player2, "\n")
    return


# determines number of games to be won, to win the match
def NumberOfMatches():

    flag = False
    while flag == False:
        numMatches = input("Enter best out of ____ matches:")
        numMatches,flag = ValidateInput(numMatches)

    numMatches = int(numMatches)
    if numMatches > 10 or numMatches <= 0:
        print(numMatches, "\n")
        print("Please enter a number less than 10")
        NumberOfMatches()
    else:
        print("Best out of ", numMatches, "matches")
        return numMatches

    print("Please use a number, you friggin' idiot")
    return (NumberOfMatches())


# gets the size of the board and makes sure it's more than 4x4 and less than 10x10
def BoardSize():

    flag = False
    while flag == False:
        try:
            boardSize = input("Please enter the size of the board to be used:")
            boardSize = int(boardSize)
            flag = True
        except ValueError:
            print("You're literally the dumbest thing to walk this planet, try a number you piece of trash!")

    print("The size of the board will be ", boardSize, "x", boardSize)
    return boardSize


# Draws initial board
def DrawInitialBoard(boardSize):
    border = boardSize

    # This print is purely for aesthetic on the console to allow column numbers to line up neatly
    print(" ", end = '')

    for i in range(border):
        # the double space in the print line is purely for aesthetic on the console
        print(i, "  ", end = '')
    print("\n")

    for i in range(boardSize):
        for i in range(boardSize):
            print("--- ", end = '')
        print("\n")

    return


# makes blank 2D array that represents board
def DrawBoard(boardSize):

    rows, columns = (boardSize, boardSize)

    arr = [["---" for i in range(columns)] for j in range(rows)]
    # this is for debugging purposes only remove for final product
    #print(arr)

    return arr


# takes integer input from user, that represents what column they will place a piece
def UserInput():

    flag = False

    while flag == False:

        column = input("Please enter column number to place piece:")
        column, flag = ValidateInput(column)

    return column


# draws board to screen
def PrintBoard(array, boardSize):

    print(" ", end = '')

    for i in range(boardSize):
        print(i, "  ", end = '')
    print("\n")

    for j in range(boardSize):
        for k in range(boardSize):
            print(array[k][j], end = ' ')
        print("\n")

    return


# Checks column to make sure it isn't filled with pieces
def CheckColumn(inputColumn, array):

    flag = True

    if array[inputColumn][0] == '-X-' or array[inputColumn][0] == '-0-':
        print("invalid move use another column")
        flag = False
        return flag
    else:
        return flag


# This will check to see where the piece will go
def PlacePiece(array, inputColumn, boardSize, piece):

    for j in range(boardSize):
        if array[inputColumn][j] == '---' and array[inputColumn][j+1] != '---':
            #code will not run until you determine which piece to place
            array[inputColumn][j] = piece
            # For debugging
            #print(array)
            return array

        if array[inputColumn][boardSize-1] == '---':
            array[inputColumn][boardSize-1] = piece
            return array

        j +=  1

    return array


# Will call functions for your turn
def IsItMyTurnYet(piece, array, boardSize):

    notFull = False


    while notFull == False:

        # Makes sure you don't select an element outside of the index of the board array
        try:
            inputColumn = int(UserInput())
            notFull = bool(CheckColumn(inputColumn, array))
        except IndexError:
            print("I don't know how you made it this far in life without being hit for being so miserably deficient as an adult")
            print("You have to choose a number that's actually on the screen")
            notFull == False


    array = PlacePiece(array, inputColumn, boardSize, piece)

    if piece == '-X-':
        piece = '-0-'
    else:
        piece = '-X-'

    return piece, array


def DidYouWinVeritcally(boardSize, gameWon, P1Wins, P2Wins, array):

    try:

        for j in range(boardSize):
            for i in range(boardSize):
                if array[j][i] == '-X-' and array[j][i+1] == '-X-' and array[j][i+2] == '-X-' and array[j][i+3] == '-X-':
                    gameWon = True
                    P1Wins += 1
                    return gameWon, P1Wins, P2Wins
                elif array[j][i] == '-0-' and array[j][i+1] == '-0-' and array[j][i+2] == '-0-' and array[j][i+3] == '-0-':
                    gameWon = True
                    P2Wins += 1
                    return gameWon, P1Wins, P2Wins

    except IndexError:

        return gameWon, P1Wins, P2Wins

    return gameWon, P1Wins, P2Wins


def DidYouWinHorizontally(boardSize, array, gameWon, P1Wins, P2Wins):

    try:

        for j in range(boardSize):
            for i in range(boardSize):
                if array[i][j] == '-X-' and array[i+1][j] == '-X-' and array[i+2][j] == '-X-' and array[i+3][j] == '-X-':
                    P1Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins
                elif array[i][j] == '-0-' and array[i+1][j] == '-0-' and array[i+2][j] == '-0-' and array[i+3][j] == '-0-':
                    P2Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins
    except IndexError:

        return gameWon, P1Wins, P2Wins

    return gameWon, P1Wins, P2Wins


def DidYouWinDiagonally(boardSize, array, gameWon, P1Wins, P2Wins):

    for i in range(boardSize):
        for j in range(boardSize):
            try:
                if array[i][j] == '-X-' and array[i+1][j+1] == '-X-' and array[i+2][j+2] == '-X-' and array[i+3][j+3] == '-X-':
                    P1Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins
                elif array[i][j] == '-0-' and array[i+1][j+1] == '-0-' and array[i+2][j+2] == '-0-' and array[i+3][j+3] == '-0-':
                    P2Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins
                elif array[i][j] == '-X-' and array[i+1][j-1] == '-X-' and array[i+2][j-2] == '-X-' and array[i+3][j-3] == '-X-':
                    P1Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins
                elif array[i][j] == '-0-' and array[i-1][j+1] == '-0-' and array[i-2][j+2] == '-0-' and array[i-3][j+3] == '-0-':
                    P2Wins += 1
                    gameWon = True
                    return gameWon, P1Wins, P2Wins

            except IndexError:
                continue

    return gameWon, P1Wins, P2Wins


# Checks and returns who won
def WhoWon(gameWon, boardSize, array, P1Wins, P2Wins):

    gameWon = False

    gameWon, P1Wins, P2Wins = DidYouWinVeritcally(boardSize, gameWon, P1Wins, P2Wins, array)
    if gameWon == True:
        return gameWon, P1Wins, P2Wins
    gameWon, P1Wins, P2Wins = DidYouWinHorizontally(boardSize, array, gameWon, P1Wins, P2Wins)
    if gameWon == True:
        return gameWon, P1Wins, P2Wins
    gameWon, P1Wins, P2Wins = DidYouWinDiagonally(boardSize, array, gameWon, P1Wins, P2Wins)
    if gameWon == True:
        return gameWon, P1Wins, P2Wins

    return gameWon, P1Wins, P2Wins


# resets the array and draws the board for the next game
def StartNextGame(array, boardSize, P1, P2):

    array = DrawBoard(boardSize)

    PrintPlayerName(P1, P2)
    DrawInitialBoard(boardSize)

    return array


# Starts the first game
def StartGame():

    P1, P2 = GetPlayerName()
    matches = NumberOfMatches()
    boardSize = BoardSize()

    # checks to make board size is correct size
    while boardSize > 10 or boardSize < 4:
        print("Alright, obviously you following directions is much like trying to get North Korea to feed it's citizens")
        print("Enter a number greater than 4 and less than 10")
        boardSize = BoardSize()

    array = DrawBoard(boardSize)
    piece = "-X-"
    piece = str(piece)

    PrintPlayerName(P1, P2)
    DrawInitialBoard(boardSize)

    return P1, P2, matches, boardSize, array, piece


def WinnerScreen():

    print("Congratulations! You won the match!")
    print("You are smarter and better than your friend/rival in every conceivable way.")
    return


#this should keep track of who's turn it is and number of games won
def GameState():

    P1Wins = 0
    P2Wins = 0
    matchWon = 0
    columnFlag = False
    gameWon = False

    P1, P2, matches, boardSize, array, piece = StartGame()

    while matchWon == 0:

        while gameWon == False:
            piece, array = IsItMyTurnYet(piece, array, boardSize)
            PrintPlayerName(P1, P2)
            PrintBoard(array, boardSize)
            gameWon, P1Wins, P2Wins = WhoWon(gameWon, boardSize, array, P1Wins, P2Wins)

        print("you definitely won this game and are super great and have massive testicles")

        # this is so that the flag is reset for the next loop iteration
        gameWon = False

        array = StartNextGame(array, boardSize, P1, P2)

        if P1Wins == matches or P2Wins == matches:
            matchWon = 1

    WinnerScreen()

    return


def main():

    GameState()

    return

if __name__ == '__main__':
    main()
