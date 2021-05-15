import json

import src.simian_lambda.lambda_function as test_simian


def test_empty():
    assert test_simian.is_simian([]) == 400


def test_invalid_square(invalid_square):
    assert test_simian.is_simian(invalid_square) == 400


def test_invalid_table(invalid_table):
    assert test_simian.is_simian(invalid_table) == 400


def test_short_table(short_table):
    assert test_simian.is_simian(short_table) == 403


def test_human_4(human_4):
    assert test_simian.is_simian(human_4) == 403


def test_human_6(human_6):
    assert test_simian.is_simian(human_6) == 403


def test_human_10(human_10):
    assert test_simian.is_simian(human_10) == 403


def test_horizontal_simian_4_A(simian_4_A):
    assert test_simian.verify_by_line(simian_4_A) is True


def test_vertical_simian_4_A(simian_4_A):
    vertical_table = test_simian.get_vertical_table(simian_4_A)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_4_A(simian_4_A):
    size = len(simian_4_A)
    diagonal_table = test_simian.get_diagonal_table(simian_4_A, size, 'r')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_horizontal_simian_4_T(simian_4_T):
    assert test_simian.verify_by_line(simian_4_T) is True


def test_vertical_simian_4_T(simian_4_T):
    vertical_table = test_simian.get_vertical_table(simian_4_T)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_4_T(simian_4_T):
    size = len(simian_4_T)
    diagonal_table = test_simian.get_diagonal_table(simian_4_T, size, 'r')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_horizontal_simian_4_C(simian_4_C):
    assert test_simian.verify_by_line(simian_4_C) is True


def test_vertical_simian_4_C(simian_4_C):
    vertical_table = test_simian.get_vertical_table(simian_4_C)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_4_C(simian_4_C):
    size = len(simian_4_C)
    diagonal_table = test_simian.get_diagonal_table(simian_4_C, size, 'l')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_horizontal_simian_4_G(simian_4_G):
    assert test_simian.verify_by_line(simian_4_G) is True


def test_vertical_simian_4_G(simian_4_G):
    vertical_table = test_simian.get_vertical_table(simian_4_G)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_4_G(simian_4_G):
    size = len(simian_4_G)
    diagonal_table = test_simian.get_diagonal_table(simian_4_G, size, 'l')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_horizontal_simian_6(simian_6):
    assert test_simian.verify_by_line(simian_6) is True


def test_vertical_simian_6(simian_6):
    vertical_table = test_simian.get_vertical_table(simian_6)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_6(simian_6):
    size = len(simian_6)
    diagonal_table = test_simian.get_diagonal_table(simian_6, size, 'r')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_horizontal_simian_10(simian_10):
    assert test_simian.verify_by_line(simian_10) is True


def test_vertical_simian_10(simian_10):
    vertical_table = test_simian.get_vertical_table(simian_10)
    assert test_simian.verify_by_line(vertical_table) is True


def test_diagonal_simian_10(simian_10):
    size = len(simian_10)
    diagonal_table = test_simian.get_diagonal_table(simian_10, size, 'l')
    assert test_simian.verify_by_line(diagonal_table) is True


def test_lambda_handler_horizontal_200(event, horizontal_simian_4):
    event['body'] = json.dumps({'dna': horizontal_simian_4})
    response = test_simian.lambda_handler(event, 'context')
    assert response['statusCode'] == 200


def test_lambda_handler_vertical_200(event, vertical_simian_4):
    event['body'] = json.dumps({'dna': vertical_simian_4})
    response = test_simian.lambda_handler(event, 'context')
    assert response['statusCode'] == 200


def test_lambda_handler_right_diagonal_200(event, right_diagonal_simian_4):
    event['body'] = json.dumps({'dna': right_diagonal_simian_4})
    response = test_simian.lambda_handler(event, 'context')
    assert response['statusCode'] == 200


def test_lambda_handler_left_diagonal_200(event, left_diagonal_simian_4):
    event['body'] = json.dumps({'dna': left_diagonal_simian_4})
    response = test_simian.lambda_handler(event, 'context')
    assert response['statusCode'] == 200


def test_lambda_handler_403(event, human_4):
    event['body'] = json.dumps({'dna': human_4})
    response = test_simian.lambda_handler(event, 'context')
    assert response['statusCode'] == 403
