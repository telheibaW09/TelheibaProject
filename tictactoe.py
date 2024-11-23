# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                        (0, 4, 8), (2, 4, 6)]            # Diagonals
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (for a draw)
def is_board_full(board):
    return " " not in board

# Main function to play the game
def play_game():
    board = [" "] * 9  # Empty board
    current_player = "X"  # Starting with player X

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Validate move
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
