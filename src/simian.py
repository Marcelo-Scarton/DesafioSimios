sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']


def is_simian(table):
    if len(table[0]) < 4:
        return False
    # horizontal
    if verify_by_line(table):
       return True
    # vertical
    vertical_table = get_vertical_table(table)
    if verify_by_line(vertical_table):
        return True
    return False


def verify_by_line(table):
    for line in table:
        for sequence in sequences:
            if sequence in line:
                print(line)
                return True
    return False


def get_vertical_table(table):
    vertical_table = []
    aux_table = list(zip(*table))
    for line in aux_table:
        value =  "".join(list(line))
        vertical_table.append(value)
    return vertical_table


if __name__ == '__main__':
    print(is_simian(['CTGAGA', 'CTGAGC', 'TATTGT', 'AGAGGG', 'CCTCTA', 'TCACTG']))
