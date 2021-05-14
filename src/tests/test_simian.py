import json

from src.simian_lambda.lambda_function import lambda_handler, is_simian


def test_lambda_handler_200(event, horizontal_simian_4):
    event['body'] = json.dumps({'dna': horizontal_simian_4})
    response = lambda_handler(event, 'context')
    assert response['statusCode'] == 200


def test_lambda_handler_403(event, human_4):
    event['body'] = json.dumps({'dna': human_4})
    response = lambda_handler(event, 'context')
    assert response['statusCode'] == 403


def test_empty():
    assert is_simian([]) == 400


def test_invalid_length(invalid_length):
    assert is_simian(invalid_length) == 403


def test_invalid_square(invalid_square):
    assert is_simian(invalid_square) == 400


def test_invalid_table(invalid_table):
    assert is_simian(invalid_table) == 400


def test_human_4(human_4):
    assert is_simian(human_4) == 403


def test_horizontal_simian_4(horizontal_simian_4):
    assert is_simian(horizontal_simian_4) == 200


def test_vertical_simian_4(vertical_simian_4):
    assert is_simian(vertical_simian_4) == 200


def test_right_diagonal_simian_4(right_diagonal_simian_4):
    assert is_simian(right_diagonal_simian_4) == 200


def test_left_diagonal_simian_4(left_diagonal_simian_4):
    assert is_simian(left_diagonal_simian_4) == 200
