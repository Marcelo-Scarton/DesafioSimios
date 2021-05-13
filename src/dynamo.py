import boto3


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
