import pytest


@pytest.fixture(scope="module")
def event():
    return {"body": None}


@pytest.fixture(scope="function")
def invalid_square():
    return ['ATCG', 'AAAT', 'TTTC', 'CGG']


@pytest.fixture(scope="function")
def invalid_table():
    return ['ATCG', 'AAAA', 'TTTC', 'CGGX']


@pytest.fixture(scope="function")
def short_table():
    return ['AAA', 'TTT', 'CCC']


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


@pytest.fixture(scope="function")
def human_4():
    return ['ATCG', 'AAAT', 'TTTC', 'CGGG']


@pytest.fixture(scope="function")
def human_6():
    return ['ATCGAT', 'TAGGCG', 'TAGCAT', 'AGCCCA', 'AGTCTC', 'AGTTTA']


@pytest.fixture(scope="function")
def human_10():
    return [
        'ATCGATCGAT',
        'CACACACACA',
        'GTGTGTGTGT',
        'CACACACACA',
        'GTGTGTGTGT',
        'CACACACACA',
        'GTGTGTGTGT',
        'CACACACACA',
        'GTGTGTGTGT',
        'CACACACACA'
    ]


@pytest.fixture(scope="function")
def simian_4_A():
    return ['AACG', 'AACG', 'AAAA', 'CAGA']


@pytest.fixture(scope="function")
def simian_4_T():
    return ['TTCG', 'ATCG', 'TTTT', 'CTGT']


@pytest.fixture(scope="function")
def simian_4_C():
    return ['ACCC', 'ACCG', 'CCCC', 'CCGA']


@pytest.fixture(scope="function")
def simian_4_G():
    return ['AGCG', 'AGGG', 'GGGG', 'GGGA']


@pytest.fixture(scope="function")
def simian_6():
    return ['ATCGAT', 'TACCCG', 'TAGCAT', 'ACCCCA', 'AGTCTC', 'AGTTTA']


@pytest.fixture(scope="function")
def simian_10():
    return [
        'ATCGATCGAT',
        'ATCGATCGAT',
        'ATCGATCGAT',
        'TTTTTTTTTT',
        'AAAAATAAAA',
        'CCCCTTCCCC',
        'GGGTGTTTTT',
        'TTTTTTTTTT',
        'AAAAAAAAAA',
        'CACACACACA'
    ]
