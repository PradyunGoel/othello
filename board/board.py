import pygame, sys
import time
import random
from pygame.locals import *
from change_board import *


#TODO: Have all constants here - sizes, colors, counter
#surface height, breadth
SURF_B = 800 # TODO: SURF_B, SURF_H = 800, 640, SURF, BOARD are same???
SURF_H = 640

#board heigth, breadth
BOARD_B = 640 #TODO: BOARD_B, BOARD_H = 800, 640
BOARD_H = 640

#initialising pygame and the time and music component
pygame.init()
pygame.mixer.init()

#setting up the board
board_surf = pygame.display.set_mode((SURF_B, SURF_H)) 
board_pic = pygame.image.load("board.jpg") # TODO: loaf and scale can be refactored into a function.
board_pic = pygame.transform.scale(board_pic, (BOARD_B, BOARD_H))
cells = pygame.image.load("grid.png")
cells = pygame.transform.scale(cells, (BOARD_B, BOARD_H))
menu_button = pygame.image.load("menu_button.png")
menu_button = pygame.transform.scale(menu_button, (BOARD_B//16, BOARD_H//16))
start_pic = pygame.image.load("othello_pic.jpg")
start_pic = pygame.transform.scale(start_pic, (SURF_B, SURF_H))
start_heading = pygame.image.load("othello_heading.jpg")
start_heading = pygame.transform.scale(start_heading, (SURF_B, SURF_H//7))

#setting size of each cell
cell_b = BOARD_B//8
cell_h = BOARD_H//8

#setting up each counter
wh_counter = pygame.image.load('white_piece.png')
wh_counter = pygame.transform.scale(wh_counter, (cell_b, cell_h))
bl_counter = pygame.image.load('black_piece.png')
bl_counter = pygame.transform.scale(bl_counter, (cell_b, cell_h))

#setting up the legal move indicator
pos_move = pygame.image.load("pos_frame.png")
pos_move = pygame.transform.scale(pos_move, (cell_b, cell_h))

#colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (18, 164, 217)
indigo = (9, 49, 69)
salmon = (250,128,114)
powder = (158, 185, 212)
magenta = (246, 83, 166)
chocolate = (123, 63, 0)
dark_green = (10, 145, 0)
grey = (128, 128, 128)
green = (192, 255, 0)
kelly = (163, 184, 108)
daisy = (239, 212, 105)
raven = (55, 61, 63)
yellow = (226, 216, 16)
red = (255, 0, 0)
orange = (210, 96, 26)
olive = (128, 128, 0)

#score variable-index0 = white, index1 = black
score = [0, 0]

#tracking3 the player currently playing(0-white, 1-black)
turn = 0 # TODO: BLACK/WHITE

#tracking each counter on the board(1-white, 2-black, 0-nothing)
WHITE = 1
BLACK = 2
EMPTY = 0 # TODO: -1?
counters = []
default = []

#tracking how many spots have been taken up on the board
num_done = 0

#tracking time
timer = time.time()

#tracking whether the menu is open or not
menu_on = 0

#theme variables
bg = indigo
text_col = daisy
wh_ring = orange
bl_ring = green

#initialising the board to empty in all cells
'''for i in range(8): # TODO: Define a constant for 8
    counters.append([EMPTY]*8)
    default.append([EMPTY]*8)
#print(counters)
'''

#make this a dictionary of themes
#function to set the theme
def set_theme(theme = "default"):
    global text_col, bg, wh_ring, bl_ring
    if theme == "light":
        text_col = indigo
        bg = daisy
        wh_ring = orange
        bl_ring = green
    elif theme == "xmas":
        text_col = dark_green
        bg = red
        wh_ring = dark_green
        bl_ring = dark_green
    else:
        text_col = daisy
        bg = indigo
        wh_ring = orange
        bl_ring = green


#function to fill in the board with the counters
def fill_board():
    board_surf.blit(board_pic, (0, 0))
    board_surf.blit(cells, (0, 0))
    for row in range(8):
        for col in range(8):
            # blit the counter on the board for each cell
            if board[row][col] == WHITE:
                board_surf.blit(wh_counter, (row*cell_b, col*cell_h))
            if board[row][col] == BLACK:
                board_surf.blit(bl_counter, (row*cell_b, col*cell_h))
    pygame.display.update()


def change_board(game_board, x, y):
    #to be done by pranjal
    #returns the new board
    #randomly changing the board
    # ----------
    for i in range(8):
        for j in range(8):
            if game_board[i][j] == 1 or game_board[i][j] == 0:
                game_board[i][j] = random.randint(0, 1)
    # ----------

    game_board[x][y] = turn
    wh_sc, bl_sc = 0, 0
    for i in range(8):
        wh_sc += game_board[i].count(WHITE)
        bl_sc += game_board[i].count(BLACK)
    score[0] = wh_sc
    score[1] = bl_sc
    print(score)
    return game_board


def show_score():
    global num_done
    font = pygame.font.SysFont(None, 24)
    '''if turn == WHITE:
        pygame.draw.ellipse(board, green, (660, 10, cell_b, cell_h), 2)
        player = 'WHITE'
    else:
        pygame.draw.ellipse(board, green, (660, 10+2*cell_h, cell_b, cell_h), 2)
        player = 'BLACK'
        '''
    num_done = score[WHITE-1]+score[BLACK-1]
    wh_score = font.render(str(score[WHITE-1]), True, indigo)
    bl_score = font.render(str(score[BLACK-1]), True, green)
    progress = font.render("Game progress", True, text_col)
    #playing = font.render(player+"'s turn!", True, salmon)
    pygame.draw.rect(board_surf, bg, (640, 0, 160, 640))
    pygame.draw.rect(board_surf, text_col, (640, 0, 160, 640), 5)
    pygame.draw.rect(board_surf, text_col, (660, 20+7*cell_h, num_done*120//64, cell_h//4))
    pygame.draw.rect(board_surf, text_col, (660, 20+7*cell_h, 120, cell_h//4), 1)
    #board_surf.blit(wh_score, (660, cell_h+20))
    #board_surf.blit(bl_score, (660, 3*cell_h+20))
    board_surf.blit(progress, (660, 7*cell_h))
    #board.blit(playing, (660, 20+4*cell_h))
    board_surf.blit(menu_button, (660, 50+5*cell_h))
    board_surf.blit(wh_counter, (660, 10))
    board_surf.blit(bl_counter, (660, 10+2*cell_h))
    if col == WHITE: #TODO: Use same color to indicate the turn
        pygame.draw.ellipse(board_surf, wh_ring, (660+4, 10+2, cell_b-6, cell_h-6), 8) #magenta, 
    else:
        pygame.draw.ellipse(board_surf, bl_ring, (660+1, 10+2*cell_h+1, cell_b-5, cell_h-5), 8)
    board_surf.blit(wh_score, (10+660+cell_b//3, cell_h//2))
    board_surf.blit(bl_score, (10+660+cell_b//3, 2*cell_h+cell_h//2))


#function to check if the board is full
def game_over():
    for i in range(8):
        if EMPTY in board[i]:
            return False
    return True


def clicked(x, y, b, h, mouse_x, mouse_y):
    if x<mouse_x<x+b and y<mouse_y<y+h:
        return True
    return False


#function to show the menu
def show_menu():
    global menu_on
    menu_on = 1
    font = pygame.font.SysFont(None, 32)
    '''
    if menu_on == 0: # TODO: Use a boolean value
        menu_on = 1
    else:
        menu_on = 0
    '''

    menu_heading = font.render("MENU", True, white)
    quit_button = font.render("QUIT GAME", True, bg)
    resume_button = font.render("RESUME", True, bg)
    reset_button = font.render("RESET GAME", True, bg)

    pygame.draw.rect(board_surf, bg, (BOARD_B//5, BOARD_H//5, 3*BOARD_B//5, 3*BOARD_H//5))
    pygame.draw.rect(board_surf, text_col, (BOARD_B//5, BOARD_H//5, 3*BOARD_B//5, 3*BOARD_H//5), 3)
    board_surf.blit(menu_heading, (4*BOARD_B//9, BOARD_H//5+BOARD_H//25))
    pygame.draw.rect(board_surf, text_col, (BOARD_B//5+BOARD_B//25, BOARD_H//5+3*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25))
    board_surf.blit(quit_button, (BOARD_B//5+BOARD_B//20, BOARD_H//5+3*BOARD_H//25+BOARD_H//25))
    pygame.draw.rect(board_surf, text_col, (BOARD_B//5+BOARD_B//25, BOARD_H//5+7*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25))
    board_surf.blit(resume_button, (BOARD_B//5+BOARD_B//20, BOARD_H//5+7*BOARD_H//25+BOARD_H//25))
    pygame.draw.rect(board_surf, text_col, (BOARD_B//5+BOARD_B//25, BOARD_H//5+11*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25))
    board_surf.blit(reset_button, (BOARD_B//5+BOARD_B//20, BOARD_H//5+11*BOARD_H//25+BOARD_H//25))
    pygame.display.update()

    print("hi")

    while menu_on:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse")
                x, y = pygame.mouse.get_pos()
                if 660<x<660+cell_b//2 and 50+5*cell_h<y<50+5*cell_h+cell_h//2:
                    menu_on = 0
                    fill_board()
                    show_legal(posmove(board, col))
                    print("MENU CLOSING")
                if clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+3*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = 0
                    pygame.quit()
                    print("QUITTING")
                    sys.exit()
                elif clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+7*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = 0
                    fill_board()
                    show_legal(posmove(board, col))
                    print("RESUMING")
                elif clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+11*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = 0
                    reset()
                    fill_board()
                    show_legal(posmove(board, col))
                    print("RESETTING")


#function to reset the game
def reset():
    global board, col, pos, score, turn, num_done
    board = initialize()
    col = 2
    score = [0, 0]
    pos = [-1, -1]
    #num_done = 0
    #board_surf.blit(board_pic, (0, 0))
    #board_surf.blit(cells, (0, 0))
    #show_score()
    #pygame.display.update()


#function to show the possible moves
def show_legal(pos_moves):
    for move in pos_moves:
        board_surf.blit(pos_move, (move[0]*cell_b, move[1]*cell_h))
    pygame.display.update()


#displaying the intial screen
#tracking whether the user has started the game
start_game = 0
font = pygame.font.SysFont(None, 32)
start_mssg = font.render("CLICK ANYWHERE TO CONTINUE", True, raven)

board_surf.blit(start_pic, (0, 0))
board_surf.blit(start_heading, (0, 0))
pygame.draw.rect(board_surf, olive, (SURF_B//5, 2*SURF_H//3, 3*SURF_B//5, SURF_H//11))
board_surf.blit(start_mssg, (SURF_B//5+SURF_B//18, SURF_H//3+SURF_H//5+3*SURF_H//25+SURF_H//25))
pygame.display.update()

while(not(start_game)):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game = 1

#setting the theme to default(temporary)
#u_theme = input("Enter the theme: ")
#set_theme(u_theme)
set_theme("default")

board_surf.blit(board_pic, (0, 0))   # TODO: blit and update can be refactored into a function 
board_surf.blit(cells, (0, 0))       # TODO: board and cells are always blitted together. Can be refactored into a function draw_board() or something
fill_board()
show_score()
pygame.display.update()

while True:
    if posmove(board, col) == []:
        print("You must pass! No legal moves")
        col = 3-col
        show_score()
        pygame.display.update()
        continue
    else:
        show_legal(posmove(board, col))

    pos = [-1, -1]

    #print(posmove(board, col), "is the list of possible moves for col =",col)

    while not legalmove(board, pos, col):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_cell, y_cell = x//cell_b, y//cell_h
                if x_cell < 8 and y_cell < 8:
                    pos = [x_cell, y_cell]
                elif 660<x<660+cell_b//2 and 50+5*cell_h<y<50+5*cell_h+cell_h//2:
                    print("MENU OPENING")
                    show_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #x = int(input())
        #y = int(input())
        #waits till some correct possible co-ordinates picked

    flipdisc, numdisc = checkdiscs(board, pos, col)

    makmo(pos, col)
    col = 3-col

    fill_board()

    wh_score = 0
    bl_score = 0
    for row in board:
        wh_score += row.count(WHITE)
        bl_score += row.count(BLACK)
    score = [wh_score, bl_score]

    show_score()

    if nomove(board):
        if score[WHITE-1] > score[BLACK-1]:
            print("White wins!")
        elif score[BLACK-1] > score[WHITE-1]:
            print("Black wins!")
        else:
            print("Well played! It's a draw.")
        print("MENU")
        break

    #reset()
    pygame.display.update()
    
    '''for event in pygame.event.get():
        #later add condition to check for mouseclick only once the menu has been closed
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x_cell, y_cell = x//cell_b, y//cell_h
            print("cell", x_cell, y_cell) # TODO: In one print
            print(x, y)
            if not(menu_on):
                if x_cell < 8 and y_cell < 8:
                    if board[x_cell][y_cell] == 2:
                        #board = change_board(counters, x_cell, y_cell)
                        fill_board()
                        if turn == WHITE: # TODO: BLACK/WHITE
                            turn = BLACK
                        else:
                            turn = WHITE
            if 660<x<660+cell_b//2 and 50+5*cell_h<y<50+5*cell_h+cell_h//2:
                show_menu()
                print("MENU OPENING")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_over():
        if score[WHITE-1] > score[BLACK-1]:
            print("White wins!")
        elif score[BLACK-1] > score[WHITE-1]:
            print("Black wins!")
        else:
            print("Well played! It's a draw.")
        print("MENU")
        #reset()
    ''' 

#board_surf.blit(board_pic, (0, 0))
#board_surf.blit(cells, (0, 0))
pygame.display.update() # TODO: Why multiple display.update() calls in various functions. 1 here end of the while loop is sufficient?
time.sleep(5)
