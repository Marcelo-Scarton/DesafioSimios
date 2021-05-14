from src.stats_lambda.lambda_function import lambda_handler

def test_success():
    response = lambda_handler('event', 'context')
    assert response['statusCode'] == 200