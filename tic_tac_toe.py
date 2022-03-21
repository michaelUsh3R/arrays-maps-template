# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: DID I WIN TIC-TAC-TOE?
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 3: Arrays & Maps

# takes a player character and a 2-dimensional
# array as parameters and returns whether the
# player won the game
# HINT: What does a boolean accumulator look like?
def did_I_win_2D(player, board): #checks for winner
    if len(board) != 3:
        return False
    elif len(board[0]) != 3:
        return False
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def print_2D_board(b): #prints the board
    for i in range(len(b)):
        print(b[i])

def main(): #runs and tells which side won
    boards = [ ["X"] * 10 ] * 10

    print("X won?", did_I_win_2D("X", boards))
    print("O won?", did_I_win_2D("O", boards))

if __name__ == '__main__':
    main()