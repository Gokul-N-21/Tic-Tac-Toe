import random

#creating a skeleton for the board
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('--+---+--')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('--+---+--')
    print(f'{board[7]} | {board[8]} | {board[9]}')

def choose_first():
    player = random.randint(0,1)
    if player == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if position > 9 or board[position] != ' ':
        return False
    else:
        return True
    
def full_check(board):
    for val in board[1:]:
        if val == ' ':
            return False
    return True

#Update values on the particular position
def place_marker(board, marker, position):
    if space_check(board,position):
        board[position] = marker
    else:
        print('Invalid position!! Please try another position')

#Check the winning conditions
def win_check(board, mark):
    return (
        # Rows
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        # Columns
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        # Diagonals
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)
    )

def replay():
    choice = input('Do you want to play the game again? [Yes | No]: ').lower().strip()
    return choice == 'yes'

def computer_move(board):
    # 1. Check if the computer can win in the next move
    for i in range(1, 10):
        if board[i] == ' ':
            temp_board = board[:] # Copy board
            temp_board[i] = 'O'
            if win_check(temp_board, 'O'):
                return i

    # 2. Check if the player is about to win and block them
    for i in range(1, 10):
        if board[i] == ' ':
            temp_board = board[:] # Copy board
            temp_board[i] = 'X'
            if win_check(temp_board, 'X'):
                return i

    # 3. Otherwise, pick a random available spot
    spaces = [i for i in range(1, 10) if board[i] == ' ']
    return random.choice(spaces)

def run_game():
    while True: # Outer loop for Replay
        print("Welcome to the TIC TAC TOE Game!!")
        board = [' '] * 10
        turn = choose_first() 
        print(turn + ' will go first.')
        gameon = True

        while gameon: # Inner loop for the current match
            if turn == 'Player 1':
                display_board(board)
                
                # Input validation loop for Human
                while True:
                    try:
                        position = int(input("Player 1 (X), choose (1-9): "))
                        if position in range(1, 10):
                            break
                        else:
                            print("Please choose a number between 1 and 9.")
                    except ValueError:
                        print("Invalid input!! Please enter a number.")

                if space_check(board, position):
                    place_marker(board, 'X', position)
                    if win_check(board, 'X'):
                        display_board(board)
                        print('Congratulations! Player 1 has won!')
                        gameon = False
                    elif full_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        gameon = False
                    else:
                        turn = 'Player 2'
                else:
                    print("That spot is taken! Try again.")

            else:
                # COMPUTER TURN (Player 2)
                print("Computer is thinking...")
                position = computer_move(board) # Pass the board here
                
                # No try/except needed for computer
                place_marker(board, 'O', position)
                
                if win_check(board, 'O'):
                    display_board(board)
                    print('The Computer has won!')
                    gameon = False
                elif full_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    gameon = False
                else:
                    turn = 'Player 1'

        if not replay():
            print("Thanks for playing!")
            break
        
# Execute the game
if __name__ == "__main__":
    run_game()
