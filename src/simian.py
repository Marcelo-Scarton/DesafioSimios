import re

sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']


def is_simian(table):
    if len(table) < 4:
        return False
    if not is_square(table):
        return False
    if not is_valid(table):
        return False
    # horizontal
    if verify_by_line(table):
        return True
    # vertical
    vertical_table = get_vertical_table(table)
    if verify_by_line(vertical_table):
        return True
    # right diagonal
    right_diagonal_table = get_diagonal_table(table, "r")
    if verify_by_line(right_diagonal_table):
        return True
    # left diagonal
    left_diagonal_table = get_diagonal_table(table, "l")
    if verify_by_line(left_diagonal_table):
        return True
    return False


def is_square(table):
    size = len(table)
    for line in table:
        if len(line) != size:
            return False
    return True


def is_valid(table):
    for line in table:
        test_line = re.findall("[^ATCG]", line)
        if test_line:
            return False
    return True


def verify_by_line(table):
    for line in table:
        for sequence in sequences:
            if sequence in line:
                return True
    return False


def get_vertical_table(table):
    vertical_table = []
    aux_table = list(zip(*table))
    for line in aux_table:
        value = "".join(list(line))
        vertical_table.append(value)
    return vertical_table


def get_diagonal_table(table, direction):
    diagonal_table = []
    size = len(table)
    for i in range(size):
        beginning = i * ' ' if direction == 'l' else (size - i - 1) * ' '
        end = i * ' ' if direction == 'r' else (size - i - 1) * ' '
        value = beginning + table[i] + end
        count = value.count(" ")
        if (len(value) - count) >= 4:
            diagonal_table.append(value)
    return get_vertical_table(diagonal_table)
