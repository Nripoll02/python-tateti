# Define the board as a list of lists with "-" representing empty spaces
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# Define the players and their symbol
player1 = "X"
player2 = "O"

# Define a function to print the current state of the board
def print_board():
    for row in board:
        print(" ".join(row))

# Define a function to check if the game is over
def game_over():
    # Check if any of the rows have all the same symbol
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return True
    
    # Check if any of the columns have all the same symbol
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return True
    
    # Check if either of the diagonals have all the same symbol
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-") or \
       (board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-"):
        return True
    
    # If none of the above conditions are met, the game is not over
    return False

# Define a function to play a turn
def play_turn(player):
    # Print the current state of the board
    print_board()
    
    # Prompt the user to enter their move
    print("Player", player, ": Enter your move as 'row,column' (e.g. 1,3)")
    move = input()
    
    # Parse the move and update the board
    row, col = move.split(",")
    row, col = int(row) - 1, int(col) - 1
    board[row][col] = player

# Define a function to play the game
def play_game():
    # Keep playing turns until the game is over
    while not game_over():
        play_turn(player1)
        if game_over():
            break
        play_turn(player2)
    
    # Print the final state of the board
    print_board()
    
    # Print the result of the game
    if game_over():
        print("Player", player1 if board[1][1] == player1 else player2, "wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()
