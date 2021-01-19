gameTable = [[0,2,0],[0,1,0],[0,0,1]]

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

printGameTable(gameTable)