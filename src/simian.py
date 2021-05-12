sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']


def is_simian(table):
    if len(table[0]) < 4:
        return False
    if verify_horizontal(table):
        return True
    else:
        return False


def verify_horizontal(table):
    for line in table:
        for sequence in sequences:
            if sequence in line:
                return True
    return False


if __name__ == '__main__':
    print(is_simian(['CTGAGA', 'CTGAGC', 'TATTGT', 'AGAGGG', 'CCCCTA', 'TCACTG']))
