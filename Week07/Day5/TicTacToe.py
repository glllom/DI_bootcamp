from functools import reduce
table = [[' '] * 3 for _ in range(3)]


def show_table():
    print()
    print('***************')
    print(f'*  {table[0][0]} | {table[0][1]} | {table[0][2]}  *')
    print('* ---|---|--- *')
    print(f'*  {table[1][0]} | {table[1][1]} | {table[1][2]}  *')
    print('* ---|---|--- *')
    print(f'*  {table[2][0]} | {table[2][1]} | {table[2][2]}  *')
    print('***************')


def clean_table():
    global table
    table = [[' '] * 3 for _ in range(3)]


def check_if_win():
    #  check rows
    for row in table:
        if row[0] == row[1] == row[2] in ['X', '0']:
            return True
    #  check columns
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i] in ['X', '0']:
            return True
    #  check diagonals
    if table[0][0] == table[1][1] == table[2][2] in ['X', '0'] or table[2][0] == table[1][1] == table[0][2] in ['X', '0']:
        return True
    return False


def if_there_are_empty_cells():
    return reduce((lambda a, b: a+b), [row.count(' ') for row in table])


def game_over(current_player):
    if check_if_win():
        current_player = current_player % 2 + 1  # changing back
        print(f"Player {current_player} Wins!")
        return True
    if not if_there_are_empty_cells():
        print("Draw")
        return True
    return False


def new_turn(current_player):
    print(f"Player {current_player}'s turn.")
    column = input("Enter column: ")
    row = input("Enter row: ")
    if column not in ['1', '2', '3'] or row not in ['1', '2', '3'] or table[int(row)-1][int(column)-1] != ' ':
        print(f"Place ({column}, {row}) is not available")
        return current_player
    table[int(row)-1][int(column)-1] = ('X' if current_player == 1 else '0')
    show_table()
    current_player = current_player % 2 + 1   # 1 -> 2, and 2 -> 1
    return current_player


def start_new_game():
    #  Player1 - X, Player2 -0
    clean_table()
    show_table()
    current_player = 1
    print("Player1 - X, Player2 -0")
    current_player = new_turn(current_player)
    while not game_over(current_player):
        current_player = new_turn(current_player)

    print("Bye-bye")


start_new_game()
