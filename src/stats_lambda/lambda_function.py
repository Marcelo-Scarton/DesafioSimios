import json
import boto3

from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(stats())
    }


def stats():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('meli')
    mutant = table.scan(
        FilterExpression=Key('type').eq(1)
    )
    human = table.scan(
        FilterExpression=Key('type').eq(0)
    )
    count_mutant_dna = len(mutant['Items'])
    count_human_dna = len(human['Items'])
    ratio = count_mutant_dna / count_human_dna
    return {
        "count_mutant_dna": count_mutant_dna,
        "count_human_dna": count_human_dna,
        "ratio": round(ratio, 2)
    }
