import os

# cross = '┼'
# horizontal_line = '─'
# vertical_line = '│'

squares_orig = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = squares_orig
xIsNext = True


def is_complete():
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for square in squares:
        if square in squares_orig:
            break
    else:
        return 'tie'

    for line in lines:
        a, b, c = line
        if squares[a] and squares[a] == squares[b] and squares[a] == squares[c]:
            return squares[a]
    return False


def draw_grid(squares):
    grid = f""" ┌───┬───┬───┐
 │ {squares[0]} │ {squares[1]} │ {squares[2]} │
 ├───┼───┼───┤
 │ {squares[3]} │ {squares[4]} │ {squares[5]} │
 ├───┼───┼───┤
 │ {squares[6]} │ {squares[7]} │ {squares[8]} │
 └───┴───┴───┘"""
    print(grid)


def remove_grid():
    grid_to_remove = f""" ┌───┬───┬───┐
 │ 1 │ 2 │ 3 │
 ├───┼───┼───┤
 │ 4 │ 5 │ 6 │
 ├───┼───┼───┤
 │ 7 │ 8 │ 9 │
 └───┴───┴───┘"""
    snap_lines(grid_to_remove)


def fill_cell(i):
    global xIsNext
    # global squares
    if type(squares[i]) == int:
        squares[i] = 'X' if xIsNext else 'O'

    xIsNext = not xIsNext


def del_char():
    print('\b \b', end='')


def delete_line(line_to_delete):
    print('\033[F' + ' ' * len(line_to_delete) +
          '\b' * len(line_to_delete), end="")


def snap_lines(lines_to_delete):
    lines = lines_to_delete.split('\n')
    for line in lines:
        delete_line(line)


def get_player_turn():
    selection_is_valid = False
    player_selection_text = f"Player {'1 [X' if xIsNext else '2 [O'}] pick an open cell: "
    error_text = 'Only input a number shown above. Press ENTER to try again. '
    selection = 0

    def show_error_message():
        temp = input(error_text)
        delete_line(error_text + temp)

    while not selection_is_valid:
        selection = input(player_selection_text + ' \b')
        try:
            selection = int(selection)
            if selection not in squares_orig and selection not in squares:
                delete_line(player_selection_text)
                show_error_message()
            else:
                selection_is_valid = True

        except Exception:
            delete_line(player_selection_text)
            show_error_message()
    delete_line(player_selection_text)
    return selection


def main():
    # os.system('')

    while is_complete() == False:
        draw_grid(squares)
        player_turn = get_player_turn() - 1
        fill_cell(player_turn)
        remove_grid()

    if is_complete != 'tie':
        print(
            f"Player {'1 [X' if xIsNext else '2 [O'}] has won. Player 2 sucks!")
    else:
        print("Both of you suck! Get a life!")


if __name__ == '__main__':
    main()
