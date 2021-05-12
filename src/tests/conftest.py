import pytest


@pytest.fixture(scope="function")
def invalid_length():
    return ['AAA', 'TTT', 'CCC', 'GGG']


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
