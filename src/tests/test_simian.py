from src.simian import is_simian


def test_invalid_length(invalid_length):
    assert is_simian(invalid_length) is False


def test_invalid_square(invalid_square):
    assert is_simian(invalid_square) is False


def test_is_valid_square(valid_square):
    assert is_simian(valid_square) is True


def test_human_4(human_4):
    assert is_simian(human_4) is False


def test_horizontal_simian_4(horizontal_simian_4):
    assert is_simian(horizontal_simian_4) is True


def test_vertical_simian_4(vertical_simian_4):
    assert is_simian(vertical_simian_4) is True


def test_right_diagonal_simian_4(right_diagonal_simian_4):
    assert is_simian(right_diagonal_simian_4) is True


def test_left_diagonal_simian_4(left_diagonal_simian_4):
    assert is_simian(left_diagonal_simian_4) is True
