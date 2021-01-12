def initialize():
    #0 for no disk, 1 for red, 2 for black
    board = [[0 for i in range(8)] for j in range(8)]
    board[4][4] = board[3][3] = 1
    board[4][3] = board[3][4] = 2
    return board

def checkdiscs(board, pos, col):
    #N, S, E, W, NE, NW, SE, SW = -1
    x = pos[0]
    y = pos[1]
    numdisc = 0
    lisdisc = []

    #check Westwards
    flag = 0
    for i in range(y-1, -1, -1):
        if board[x][i] == 0:
            break
        if board[x][i] == col and flag == 0:
            for j in range(y-1, i, -1):
                lisdisc.append([x,j])
                numdisc += 1
            break

    #check Northwards
    flag = 0
    for i in range(x-1, -1, -1):
        if board[i][y] == 0:
            break
        if board[i][y] == col and flag == 0:
            for j in range(x-1, i, -1):
                lisdisc.append([j,y])
                numdisc += 1
            break
    
    #check Eastward
    flag = 0
    for i in range(y+1, 8):
        if board[x][i] == 0:
            break
        if board[x][i] == col and flag == 0:
            for j in range(y+1, i):
                lisdisc.append([x,j])
                numdisc += 1
            break

    #check Southwards
    flag = 0
    for i in range(x+1, 8):
        if board[i][y] == 0:
            break
        if board[i][y] == col and flag == 0:
            for j in range(x+1, i):
                lisdisc.append([j,y])
                numdisc += 1
            break
        
    #check SE
    xi = x+1
    yi = y+1
    while xi<8 and yi<8:
        if board[xi][yi] == 0:
            break
        if board[xi][yi] == col:
            for j in range(x+1,xi,1):
                lisdisc.append([j,y+j-x])
                numdisc += 1
            break
        xi+=1
        yi+=1

    #check NE
    xi = x-1
    yi = y+1
    while xi>=0 and yi<8:
        if board[xi][yi] == 0:
            break
        if board[xi][yi] == col:
            for j in range(x-1,xi,-1):
                lisdisc.append([j,y-j+x])
                numdisc += 1
            break
        xi-=1
        yi+=1

    #check NW
    xi = x-1
    yi = y-1
    while xi>=0 and yi>=0:
        if board[xi][yi] == 0:
            break
        if board[xi][yi] == col:
            for j in range(x-1,xi,-1):
                lisdisc.append([j,y-x+j])
                numdisc += 1
            break
        xi-=1
        yi-=1

    #check SW
    xi = x+1
    yi = y-1
    while xi<8 and yi>=0:
        if board[xi][yi] == 0:
            break
        if board[xi][yi] == col:
            for j in range(x+1,xi):
                lisdisc.append([j,y-j+x])
                numdisc += 1
            break
        xi+=1
        yi-=1
        
    return lisdisc,numdisc

def legalmove(board, pos, col):
    x = pos[0]
    y = pos[1]
    if board[x][y] != 0:
        return False
    lisdisc, numdisc = checkdiscs(board, pos, col)
    if numdisc == 0:
        return False
    return True

def posmove(board, col):
    lisa = []
    for i in range(8):
        for j in range(8):
            if legalmove(board, [i,j], col):
                lisa.append([i,j])
    return lisa

def nomove(board):
    if posmove(board, 1) == [] and posmove(board, 2) == []:
        return True
    else:
        return False

def makmo(pos, col):
    global board
    lisa = checkdiscs(board, pos, col)
    for disc in lisa:
        print(disc)
        board[disc[0]][disc[1]] = col

board = initialize()
col = 1
while(not nomove(board)):
    x = int(input())
    y = int(input())
    pos = [x,y]
    if not legalmove(board, pos, col):
        print("Illegal")
    makmo(pos, col)
    col = 1-col
