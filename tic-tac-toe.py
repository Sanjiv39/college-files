import os
import time

# Initialize the board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

# Win conditions
Win = 1
Draw = -1
Running = 0
Stop = 1

# Game state
Game = Running
Mark = 'X'

# This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print(" | | ")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print(" | | ")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")

# This Function Checks if position is empty or not
def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False
    
# This Function Checks if a player has won
def CheckWin():
    global Game
    # Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    # Vertical winning condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    # Diagonal winning condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
    # Match Tie or Draw condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and
    board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and
    board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running

# Start the game
print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print("Please Wait...")
time.sleep(1)

# Game loop
while Game == Running:
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    # Get the player's move
    choice = int(input("Enter the position between [1-9] where you want tomark: "))

    # Check if the position is valid
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

# After game over, display the result
os.system('cls' if os.name == 'nt' else 'clear')
DrawBoard()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
if player % 2 != 0:
    print("Player 1 Won")
else:
    print("Player 2 Won")