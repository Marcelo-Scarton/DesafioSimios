import pytest


@pytest.fixture(scope="function")
def invalid_length():
    return ['AAA', 'TTT', 'CCC']


@pytest.fixture(scope="function")
def invalid_square():
    return ['ATCG', 'AAAT', 'TTTC', 'CGG']


@pytest.fixture(scope="function")
def invalid_table():
    return ['ATCG', 'AAAA', 'TTTC', 'CGGX']


@pytest.fixture(scope="function")
def valid_square():
    return ['ATCG', 'ATCG', 'ATCG', 'ATCG']


@pytest.fixture(scope="function")
def human_4():
    return ['ATCG', 'AAAT', 'TTTC', 'CGGG']


@pytest.fixture(scope="function")
def horizontal_simian_4():
    return ['ATCG', 'ATCG', 'AAAA', 'GCTA']


@pytest.fixture(scope="function")
def vertical_simian_4():
    return ['ATCG', 'ATCG', 'ATTA', 'GTTA']


@pytest.fixture(scope="function")
def right_diagonal_simian_4():
    return ['ATCG', 'AACG', 'TAAA', 'GCTA']


@pytest.fixture(scope="function")
def left_diagonal_simian_4():
    return ['ATCG', 'AAGG', 'TGAA', 'GCTT']
