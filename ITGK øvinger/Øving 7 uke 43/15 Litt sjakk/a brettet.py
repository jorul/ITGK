def make_board(board_string):
    brettet = []
    for j in range (5):
        denne_raden =[]
        for i in range (5):
            if board_string[i+j*5]== '.':
                denne_raden.append(None)
            else:
                denne_raden.append(board_string[i+j*5])
        brettet.append(denne_raden)
    return brettet

board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)
for i in board:
    print (i)


def get_piece(board,x,y):
    return board[len(board)-y][x-1]

board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)
  
print(get_piece(board, 2, 1))
  # returnerer None
  
print(get_piece(board, 5, 2))
  # returnerer 'P'


def get_legal_moves(board,x,y):
    brikke = get_piece(board,x,y)
    mulige_forflyttninger =[]
    if brikke != 'p' and brikke != 'P':
        return []
    elif brikke == 'P':
        if y == 2 and get_piece(board,x,y+1) == None and get_piece(board,x,y+2) == None:
            mulige_forflyttninger.append((x,y+2))
        if get_piece(board,x,y+1) == None:
            mulige_forflyttninger.append((x,y+1))
        if get_piece(board,x+1,y+1) != None:
            if ord(get_piece(board,x+1,y+1))> 91:
                mulige_forflyttninger.append((x+1,y+1))
        if get_piece(board,x-1,y+1) != None:
            if ord(get_piece(board,x-1,y+1)) >91:
                mulige_forflyttninger.append((x-1,y+1))
    elif brikke == 'p':

        if y == 4 and get_piece(board,x,y-1) == None and get_piece(board,x,y-2) == None:
            mulige_forflyttninger.append((x,y-2))
        if get_piece(board,x,y-1) == None:
            mulige_forflyttninger.append((x,y-1))
        if get_piece(board,x+1,y-1) != None:
            if ord (get_piece(board,x+1,y-1)) < 91:
                mulige_forflyttninger.append((x+1,y-1))
        if get_piece(board,x-1,y-1) != None:
            if ord (get_piece(board,x-1,y-1)) < 91:
                mulige_forflyttninger.append((x-1,y-1))

    return mulige_forflyttninger

print(get_legal_moves(board,4,2))
print(get_legal_moves(board,2,4)) 


