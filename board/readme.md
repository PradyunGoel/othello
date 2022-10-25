## How to run venv
venv\Scripts\activate.bat


## How to setup 
python -m venv venv
pip install -r requirements.txt


## TODO
username should not be same



## Board setup
add rows and columns
get which cell has been clicked by the user


# TODO
add a noise/notification for illegal move attempt
put the score inside the circle
write othello somewhere
add winner message
take the name as input
display the winner


# Variables
board: it is an 8*8 2-D list replicating an actual board, it stores the colour of the coin at each position on the board(0-none, 1-white, 2-black)
col: it stores the player currently playing the turn(1-white, 2-black), black starts the game
score: it is a list containing 2 elements which tracks the score of the players(index0 for white and index1 for black)
FONT_BIG: big size font
FONT_MED: normal size font
start_game: it is a variable to check whether the game has been started or not
pos: it is the variable keeping track of which cell the player has selected
wh_score: score of the white player
bl_score: score of the black player


# Functions
reset: it is a function to reset the board and variables for a new game
load_image: it is a function to load and transform the image and store this image as a variable
set_theme: it is a function to set the theme of the board
fill_board: it is a function to display the board with all the pieces in the correct places
show_score: it is a function to display the part of the game which deals with the scores and to display the menu button
clicked: it is a function to check whether the user has clicked a menu option
show_menu: it is a function to display the menu and wait till a menu option has been clicked or the menu button is clicked again
show_legal: it is a function to display all the legal moves available to the player
show_winner: it is a function to display the result of the game(winner, draw)


# Bibliography
Images:
1.grid - https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F3f%2F3a%2Fa5%2F3f3aa5fc87f74007a078741b567aba44.png&imgrefurl=https%3A%2F%2Fwww.pinterest.nz%2Fpin%2F499477414904591862%2F&tbnid=dfAwYv-pn4YkvM&vet=12ahUKEwiq59ak_sfuAhXdk0sFHRkUBg4QMygBegUIARCnAQ..i&docid=goPvlzlvzXKYCM&w=800&h=800&q=grid%20images%208*8&safe=active&ved=2ahUKEwiq59ak_sfuAhXdk0sFHRkUBg4QMygBegUIARCnAQ
2.board background - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwallpapercave.com%2Fplain-green-wallpapers&psig=AOvVaw1DbWkIkHd3aGXrnSzDdGSg&ust=1612244956699000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDrl4n_x-4CFQAAAAAdAAAAABAE
3.menu button - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nicepng.com%2Fourpic%2Fu2q8w7t4q8r5a9a9_menu-menubuttom-hamburger-menu-icon-white%2F&psig=AOvVaw1UNmqvsf_s4zLsLFl2wPm3&ust=1612245473215000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDCscmAyO4CFQAAAAAdAAAAABAl

Reference websites:
1.pygame module documentation - https://www.pygame.org/docs/
2.pygame guide to drawing - https://pygame.readthedocs.io/en/latest/2_draw/draw.html
3.pygame guide to print - https://pygame.readthedocs.io/en/latest/4_text/text.html#initialize-a-font
