# By Tanut Apiwong, ID 6238396
# Sudoku Solver
# 27 SEP 2020
import math
import time

dimension = 9
sub_dimension = int(math.sqrt(dimension))
game_state = [
    0, 9, 6, 0, 4, 0, 0, 0, 0,
    0, 0, 2, 6, 0, 5, 9, 4, 7,
    4, 0, 5, 0, 9, 0, 0, 0, 6,
    6, 8, 0, 0, 0, 0, 3, 7, 4,
    5, 4, 7, 0, 0, 0, 0, 8, 2,
    3, 2, 1, 0, 7, 0, 6, 5, 0,
    0, 0, 8, 7, 0, 0, 4, 0, 3,
    9, 6, 3, 4, 8, 0, 7, 0, 5,
    1, 0, 0, 0, 5, 6, 0, 0, 8,
]
empty_box_indexes = [x for x in range(0, dimension * dimension)]


def print_board(state):
    print('  |', '  '.join(str(i) for i in range(1, dimension + 1)))
    print('-' * (dimension * 3 + 2))
    for r in range(dimension):
        offset = r * dimension
        row = state[offset: offset + dimension]
        print(r + 1, '|', '  '.join(str(e) for e in row))


def check_duplicated_number(lst):
    lst = list(filter(lambda x: x > 0, lst))
    return len(lst) != len(set(lst))


def prepare_indexes(state, indexes):
    indexes.clear()
    for i in range(len(state)):
        if state[i] == 0:
            indexes.append(i)


def fail_state_check(state):
    # Check duplicated value in each row
    for r in range(dimension):
        offset = r * dimension
        row = state[offset: offset + dimension]
        if check_duplicated_number(row):
            # print('Fail at row', row)
            return True
    # Check duplicated value in each column
    for c in range(dimension):
        col = state[c:: dimension]
        if check_duplicated_number(col):
            # print('Fail at col', col)
            return True
    # Check duplicated value in each sub-box
    for r in range(sub_dimension):
        for c in range(sub_dimension):
            offset1 = r * dimension * sub_dimension + c * sub_dimension
            offset2 = offset1 + dimension
            offset3 = offset2 + dimension
            sub = state[offset1:offset1 + 3] + state[offset2:offset2 + 3] + state[offset3:offset3 + 3]
            if check_duplicated_number(sub):
                # print('Fail at sub', sub)
                return True
    return False


def solve_sudoku(state, indexes, idx):
    if idx >= len(indexes):
        return state[:]
    for n in range(1, dimension + 1):
        new_state = state[:]
        new_state[indexes[idx]] = n
        if not fail_state_check(new_state):
            solved = solve_sudoku(new_state, indexes, idx + 1)
            if solved is not None:
                return solved


if __name__ == '__main__':
    print()
    print('Sudoku Game Board:')
    print_board(game_state)

    start_time = time.perf_counter()
    prepare_indexes(game_state, empty_box_indexes)

    print()
    print('Indexes of Empty Boxes:')
    print(empty_box_indexes)
    print()
    print('Number of boxes to be filled:', len(empty_box_indexes))

    print()
    print('Solution:')
    solved_state = solve_sudoku(game_state, empty_box_indexes, 0)
    end_time = time.perf_counter()
    print_board(solved_state)
    print('Time usage:', int((end_time - start_time) * 1000), 'ms')
