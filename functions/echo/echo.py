import json

import name


def handle(event, context):
    supplied_name = name_from_request(event)
    message_name = name.display(supplied_name)
    message = 'Guten tag {}!'.format(message_name)
    return {
        'statusCode': 200,
        'body': response_body(message)
    }


def name_from_request(event):
    if not event['queryStringParameters']:
        return None
    return event['queryStringParameters'].get('name', None)


def response_body(message):
    return json.dumps({'message': message})
