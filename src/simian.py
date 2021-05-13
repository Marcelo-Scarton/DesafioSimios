import re

from src.dynamo import insert

sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']


def is_simian(table):
    size = len(table)
    if not is_square(table, size):
        return False
    if not is_valid(table):
        return False
    if size == 0:
        return False
    if size < 4:
        insert(table, 0)
        return False
    # horizontal
    if verify_by_line(table):
        insert(table, 1)
        return True
    # vertical
    vertical_table = get_vertical_table(table)
    if verify_by_line(vertical_table):
        insert(table, 1)
        return True
    # right diagonal
    right_diagonal_table = get_diagonal_table(table, size, "r")
    if verify_by_line(right_diagonal_table):
        insert(table, 1)
        return True
    # left diagonal
    left_diagonal_table = get_diagonal_table(table, size, "l")
    if verify_by_line(left_diagonal_table):
        insert(table, 1)
        return True
    insert(table, 0)
    return False


def is_square(table, size):
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


def get_diagonal_table(table, size, direction):
    diagonal_table = []
    for i in range(size):
        beginning = i * ' ' if direction == 'l' else (size - i - 1) * ' '
        end = i * ' ' if direction == 'r' else (size - i - 1) * ' '
        value = beginning + table[i] + end
        count = value.count(" ")
        if (len(value) - count) >= 4:
            diagonal_table.append(value)
    return get_vertical_table(diagonal_table)
