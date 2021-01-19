def printCellCharacter(i):
    if i == 0:
        return " "
    elif i == 1:
        return "X"
    elif i == 2:
        return "O"

def printGameTable(gameTable):
    columnNames = [" ","1","2","3"]
    rowNames = ["A", "B", "C"]
    for c in columnNames:
        print(c, end =" ")
    print()
    for r in range(len(gameTable)):
        print(rowNames[r], end="|")
        for c in range(len(gameTable[r])):
            print(printCellCharacter(gameTable[r][c]), end="|")
        print()

def checkForRowWin(gameTable):
    for i in range(len(gameTable)):
        if gameTable[i][0] == gameTable[i][1] == gameTable[i][2] and gameTable[i][0] != 0:
            return gameTable[i][0]
    return 0

def checkForColumnWin(gameTable):
    for i in range(len(gameTable[0])):
        if gameTable[0][i] == gameTable[1][i] == gameTable[2][i] and gameTable[0][i] != 0:
            return gameTable[0][i]
    return 0

def checkForDiagonalWin(gameTable):
    if gameTable[2][0] == gameTable[1][1] == gameTable[0][2] and gameTable[2][0] != 0:
        return gameTable[2][0]
    if gameTable[0][0] == gameTable[1][1] == gameTable[2][2] and gameTable[2][2] != 0:
            return gameTable[2][2]
    return 0

def checkForDraw(gameTable):
    for i in range(len(gameTable)):
        for y in gameTable[i]:
            if y == 0:
                return False
    return True
def inputIsValid(input, gameTable):
    columnNames = ["1","2","3"]
    rowNames = ["A", "B", "C"]
    if len(input) > 2 or len(input) == 0:
        return False
    if not(input[0] in columnNames):
        return False
    if not(input[1] in rowNames):
        return False

    c = getColumnIndexFromAddress(input)
    r = getRowIndexFromAddress(input)

    if(gameTable[r][c] != 0):
        return False

    #Input passed every check
    return True

def getRowIndexFromAddress(address):
    if address[1] == "A":
        return 0
    elif address[1] == "B":
        return 1
    elif address[1] == "C":
        return 2

def getColumnIndexFromAddress(address):
    if address[0] == "1":
        return 0
    elif address[0] == "2":
        return 1
    elif address[0] == "3":
        return 2

gameTable = [[0,0,0],[0,0,0],[0,0,0]]
winner = 0
isDraw = False
playerTurn = 0 #zero for player one and one for player two
while winner == 0 and not(isDraw):
    printGameTable(gameTable)
    rowWinner = checkForRowWin(gameTable)
    columnWinner = checkForColumnWin(gameTable)
    diagonalWinner = checkForDiagonalWin(gameTable)
    winner = 0
    isDraw = checkForDraw(gameTable)
    if rowWinner != 0:
        winner = rowWinner
    elif columnWinner != 0:
        winner = columnWinner
    elif diagonalWinner != 0:
        winner = diagonalWinner
    if winner != 0:
        print("The player", winner, "has won.")
        break
    elif isDraw:
        print("It is a draw.")
        break
    else:
        print("Let's continue")
    address = str(input("Enter the address: ")).replace(" ", "")
    while not(inputIsValid(address, gameTable)):
        address = str(input("Enter the address again: ")).replace(" ", "")
    #enter the input to our array
    c = getColumnIndexFromAddress(address)
    r = getRowIndexFromAddress(address)
    if gameTable[r][c] == 0:
        gameTable[r][c] = playerTurn + 1
    playerTurn = 1 if (playerTurn == 0) else 0