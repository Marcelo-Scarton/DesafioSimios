import json
import boto3
import botocore

from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    code, body = stats()
    return {
        'statusCode': code,
        'body': json.dumps(body)
    }


def stats():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('meli')
    try:
        mutant = table.scan(
            FilterExpression=Key('type').eq(1)
        )
        human = table.scan(
            FilterExpression=Key('type').eq(0)
        )
        count_mutant_dna = len(mutant['Items'])
        count_human_dna = len(human['Items'])
        ratio = count_mutant_dna / count_human_dna
        body = {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": round(ratio, 2)
        }
        return 200, body
    except botocore.exceptions.ClientError as error:
        body = {
            "message": error.response['Error']['Message']
        }
        code = error.response['ResponseMetadata']['HTTPStatusCode']
        return code, body