import pygame, sys
import time
import random
from pygame.locals import *
from change_board import *


#reset_back()
board = initialize()
col = 2

#TODO: Have all constants here - sizes, colors, counter
#surface, board, cell height, breadth
SURF_B, SURF_H = 800, 640
BOARD_B, BOARD_H = 640, 640
CELL_B, CELL_H = BOARD_B//8, BOARD_H//8

WHITE = 1
BLACK = 2
EMPTY = 0 # TODO: -1?

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

#Globals
#score variable-index0 = white, index1 = black
score = [0, 0]
#tracking how many spots have been taken up on the board
num_done = 0
#tracking whether the menu is open or not
menu_on = False
#flag for reset
flag = 0


#function to reset the game
def reset():
    global score, num_done, menu_on, board, col, flag, pos
    score = [2, 2]
    num_done = 0
    menu_on = False
    board = initialize()
    col = 2
    flag = 0
    pos = [-1, -1]


def load_image(image, breadth, height):
    pic = pygame.image.load(f"media/{image}")
    return pygame.transform.scale(pic, (breadth, height))


#initialising pygame and the time and music component
pygame.init()
pygame.mixer.init()

FONT_BIG = pygame.font.SysFont(None, 32)
FONT_MED = pygame.font.SysFont(None, 24)

#theme variables
bg = indigo
text_col = daisy
wh_ring = orange
bl_ring = green

#setting up the board
board_surf = pygame.display.set_mode((SURF_B, SURF_H))
board_pic = load_image("board.jpg", BOARD_B, BOARD_H)
cells = load_image("grid.png", BOARD_B, BOARD_H)
menu_button = load_image('menu_button.png', BOARD_B//16, BOARD_H//16)
start_pic = load_image('othello_pic.jpg', SURF_B, SURF_H)
start_heading = load_image('othello_heading.jpg', SURF_B, SURF_H//7)
wh_counter = load_image('white_piece.png', CELL_B, CELL_H)
bl_counter = load_image('black_piece.png', CELL_B, CELL_H)
pos_move = load_image('pos_frame.png', CELL_B, CELL_H)
pos_move_white = load_image('col1.png', CELL_B, CELL_H)
pos_move_black = load_image('col2.png', CELL_B, CELL_H)

#tracking3 the player currently playing(0-white, 1-black)
turn = 0 # TODO: BLACK/WHITE


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
                board_surf.blit(wh_counter, (row*CELL_B, col*CELL_H))
            if board[row][col] == BLACK:
                board_surf.blit(bl_counter, (row*CELL_B, col*CELL_H))
    pygame.display.update()


def show_score():
    global num_done
    #font = pygame.font.SysFont(None, 24)
    num_done = score[WHITE-1]+score[BLACK-1]
    wh_score = FONT_MED.render(str(score[WHITE-1]), True, indigo)
    bl_score = FONT_MED.render(str(score[BLACK-1]), True, green)
    progress = FONT_MED.render("Game progress", True, text_col)
    #playing = font.render(player+"'s turn!", True, salmon)
    pygame.draw.rect(board_surf, bg, (640, 0, 160, 640))
    pygame.draw.rect(board_surf, text_col, (640, 0, 160, 640), 5)
    pygame.draw.rect(board_surf, text_col, (660, 20+7*CELL_H, num_done*120//64, CELL_H//4))
    pygame.draw.rect(board_surf, text_col, (660, 20+7*CELL_H, 120, CELL_H//4), 1)
    #board_surf.blit(wh_score, (660, CELL_H+20))
    #board_surf.blit(bl_score, (660, 3*CELL_H+20))
    board_surf.blit(progress, (660, 7*CELL_H))
    #board.blit(playing, (660, 20+4*CELL_H))
    board_surf.blit(menu_button, (660, 50+5*CELL_H))
    board_surf.blit(wh_counter, (660, 10))
    board_surf.blit(bl_counter, (660, 10+2*CELL_H))
    if col == WHITE:
        pygame.draw.ellipse(board_surf, wh_ring, (660+4, 10+2, CELL_B-6, CELL_H-6), 8)
    else:
        pygame.draw.ellipse(board_surf, bl_ring, (660+1, 10+2*CELL_H+1, CELL_B-5, CELL_H-5), 8)
    board_surf.blit(wh_score, (10+660+CELL_B//3, CELL_H//2))
    board_surf.blit(bl_score, (10+660+CELL_B//3, 2*CELL_H+CELL_H//2))


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
    global menu_on, flag
    menu_on = True
    #font = pygame.font.SysFont(None, 32)

    menu_heading = FONT_BIG.render("MENU", True, white)
    quit_button = FONT_BIG.render("QUIT GAME", True, bg)
    resume_button = FONT_BIG.render("RESUME", True, bg)
    reset_button = FONT_BIG.render("RESET GAME", True, bg)

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

    #print("hi")

    while menu_on:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse")
                x, y = pygame.mouse.get_pos()
                if 660<x<660+CELL_B//2 and 50+5*CELL_H<y<50+5*CELL_H+CELL_H//2:
                    menu_on = False
                    fill_board()
                    show_legal(posmove(board, col))
                    print("MENU CLOSING")
                if clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+3*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = False
                    pygame.quit()
                    print("QUITTING")
                    sys.exit()
                elif clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+7*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = False
                    fill_board()
                    show_legal(posmove(board, col))
                    print("RESUMING")
                elif clicked(BOARD_B//5+BOARD_B//25, BOARD_H//5+11*BOARD_H//25, 13*BOARD_B//25, 3*BOARD_H//25, x, y):
                    menu_on = False
                    #flag = 1
                    reset()
                    fill_board()
                    show_legal(posmove(board, col))
                    print("RESETTING")


#function to show the possible moves
def show_legal(pos_moves):
    if col == 1:
        for move in pos_moves:
            board_surf.blit(pos_move_white, (move[0]*CELL_B, move[1]*CELL_H))
    elif col == 2:
        for move in pos_moves:
            board_surf.blit(pos_move_black, (move[0]*CELL_B, move[1]*CELL_H))
    pygame.display.update()


#displaying the intial screen
#tracking whether the user has started the game
start_game = False

start_mssg = FONT_BIG.render("CLICK ANYWHERE TO CONTINUE", True, raven)

board_surf.blit(start_pic, (0, 0))
board_surf.blit(start_heading, (0, 0))
pygame.draw.rect(board_surf, olive, (SURF_B//5, 2*SURF_H//3, 3*SURF_B//5, SURF_H//11))
board_surf.blit(start_mssg, (SURF_B//5+SURF_B//18, SURF_H//3+SURF_H//5+3*SURF_H//25+SURF_H//25))
pygame.display.update()

while(not(start_game)):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game = True

#setting the theme to default(temporary)
set_theme("default")

#resetting the game
reset()

board_surf.blit(board_pic, (0, 0))
board_surf.blit(cells, (0, 0))
fill_board()
show_score()
pygame.display.update()

while True:
    if not(nomove(board)):
        if posmove(board, col) == []:
            print("You must pass! No legal moves")
            col = 3-col
            show_score()
            pygame.display.update()
            continue
        else:
            show_legal(posmove(board, col))

    pos = [-1, -1]

    flag=0
    #waits till lega move is played
    while not legalmove(board, pos, col):
        if flag == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_cell, y_cell = x//CELL_B, y//CELL_H
                if x_cell < 8 and y_cell < 8:
                    pos = [x_cell, y_cell]
                elif 660<x<660+CELL_B//2 and 50+5*CELL_H<y<50+5*CELL_H+CELL_H//2:
                    print("MENU OPENING")
                    show_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    flipdisc, numdisc = checkdiscs(board, pos, col)

    makmo(board, pos, col)
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

    pygame.display.update()

pygame.display.update() # TODO: Why multiple display.update() calls in various functions. 1 here end of the while loop is sufficient?
time.sleep(5)
