from random import randrange
board = []


def game_init():
    generate_board(board)
    game_started = input('Type "Yes" if you want to play the game: ')
    while game_started == "Yes":
        draw_move(board)
        if victory_for(board, "X"):
            print(f"The winner is X")
            game_started = "No"
            break
        if len(make_list_of_free_fields(board)) == 0:
            print(f"It's a draw")
            game_started = "No"
            break
        enter_move(board)
        if victory_for(board, "O"):
            print(f"The winner is O")
            game_started = "No"
            break
        if len(make_list_of_free_fields(board)) == 0:
            print(f"It's a draw")
            game_started = "No"
            break


def generate_board(board):
    count = 1
    for i in range(1, 4):
        row = []
        for j in range(1, 4):
            row.append(count)
            count += 1
        board.append(row)


def display_board(board):
    # Not sure if I should have added another line for more space like in the example,
    # because I like it more without the extra blank lines, but if it's a problem it's easy to fix
    to_display = ""
    for row in board:
        to_display += ("+" + "-" * 7) * 3 + "+\n"
        to_display += ("|" + " " * 7) * 3 + "|\n"
        to_display += "|" + " " * 3 + str(row[0]) + " " * 3
        to_display += "|" + " " * 3 + str(row[1]) + " " * 3
        to_display += "|" + " " * 3 + str(row[2]) + " " * 3 + "|\n"
        to_display += ("|" + " " * 7) * 3 + "|\n"

    to_display += ("+" + "-" * 7) * 3 + "+\n"
    print(to_display)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter move: "))
    free_squares = make_list_of_free_fields(board)
    need_rerun = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == board[i][j] and (i, j) in free_squares:
                board[i][j] = "O"
                display_board(board)
                victory_for(board, "O")
                need_rerun = False
                return
    if need_rerun:
        print("Please think carefully")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if type(board[i][j]) == int:
                free_squares.append(tuple([i, j]))
    return tuple(free_squares)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    win = None

    # check rows
    for row in board:
        win = True
        for i in range(len(row)):
            if row[i] != sign:
                win = False
                break
        if win:
            return win
    # check colums
    for i in range(len(board)):
        win = True
        for j in range(len(board[i])):
            if board[j][i] != sign:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(len(board)):
        if board[i][i] != sign:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != sign:
            win = False
            break
    if win:
        return win
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_squares = make_list_of_free_fields(board)
    if len(free_squares) == 9:
        board[1][1] = "X"
        display_board(board)
    else:
        did_move = False
        while did_move == False:
            i = randrange(0, 3)
            j = randrange(0, 3)
            rand_position = (i, j)
            if rand_position in free_squares:
                board[i][j] = "X"
                display_board(board)
                did_move = True


game_init()
