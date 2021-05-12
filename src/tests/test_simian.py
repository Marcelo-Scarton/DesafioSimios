from src.simian import is_simian


def test_invalid_length(invalid_length):
    assert is_simian(invalid_length) is False


def test_human(human_4):
    assert is_simian(human_4) is False


def test_horizontal_simian(horizontal_simian_4):
    assert is_simian(horizontal_simian_4) is True


def test_vertical_simian(vertical_simian_4):
    assert is_simian(vertical_simian_4) is True


def test_right_diagonal_simian(right_diagonal_simian_4):
    assert is_simian(right_diagonal_simian_4) is True


def test_left_diagonal_simian(left_diagonal_simian_4):
    assert is_simian(left_diagonal_simian_4) is True
