import json
import re
import boto3


sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']


def lambda_handler(event, context):
    data = json.loads(event["body"])
    table = data['dna']
    code = is_simian(table)
    if code == 200:
        insert_dynamodb(table, 1)
    if code == 403:
        insert_dynamodb(table, 0)
    return {
        'statusCode': code
    }


def is_simian(table):
    size = len(table)
    if not is_square(table, size):
        return 400
    if not is_valid(table):
        return 400
    if size == 0:
        return 400
    if size < 4:
        return 403
    # horizontal
    if verify_by_line(table):
        return 200
    # vertical
    vertical_table = get_vertical_table(table)
    if verify_by_line(vertical_table):
        return 200
    # right diagonal
    right_diagonal_table = get_diagonal_table(table, size, "r")
    if verify_by_line(right_diagonal_table):
        return 200
    # left diagonal
    left_diagonal_table = get_diagonal_table(table, size, "l")
    if verify_by_line(left_diagonal_table):
        return 200
    return 403


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


def insert_dynamodb(table, item_type):
    dynamodb = boto3.resource('dynamodb')
    db_table = dynamodb.Table('meli')
    dna = ''.join(table)
    db_table.put_item(
        Item={
            "dna": dna,
            "type": item_type
        }
    )
