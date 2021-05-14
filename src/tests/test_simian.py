from src.simian_lambda.lambda_function import is_simian, is_square


def test_empty():
    assert is_simian([]) == 400


def test_invalid_length(invalid_length):
    assert is_simian(invalid_length) == 403


def test_invalid_square(invalid_square):
    assert is_simian(invalid_square) == 400


def test_invalid_table(invalid_table):
    assert is_simian(invalid_table) == 400


def test_is_valid_square(valid_square):
    assert is_square(valid_square, len(valid_square)) is True


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
