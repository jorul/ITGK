def read_one_number():
    rad = int(input('Rad (1-9): '))
    kol = int(input('Kolonne(1-9): '))
    tall = int(input('Tallet (1-9): '))
    print(f'Posisjon ({rad},{kol}) inneholder nå {tall}')

def readPositionDidgit(rowNr, colNr, board):
    tall = int(input(f'Verdi for posisjon ({rowNr},{colNr}): '))
    board[rowNr-1][colNr-1] = tall
    return board

def readValidPositionDidgit(rowNr,colNr, board):
    aksept = ['0','1','2','3','4','5','6','7','8','9']
    tall = (input(f'Verdi for posisjon ({rowNr},{colNr}): '))
    while tall not in aksept:
        print('Feil! Oppgi et siffer mellom 0 og 9...')
        tall = (input(f'Verdi for posisjon ({rowNr},{colNr}): '))
    tall = int(tall)
    board[rowNr-1][colNr-1] = tall
    return board

def readSudokuBoard():
    board = [[0 for i in range(9)] for j in range(9)]
    for s in range(1,10):
        for t in range(1,10):
            readValidPositionDidgit(s,r,board)
    return board



