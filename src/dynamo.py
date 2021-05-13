import boto3

from boto3.dynamodb.conditions import Key


def insert(table, item_type):
    dynamodb = boto3.resource('dynamodb')
    db_table = dynamodb.Table('meli')
    dna = ''.join(table)
    db_table.put_item(
        Item={
            "dna": dna,
            "type": item_type
        }
    )


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
