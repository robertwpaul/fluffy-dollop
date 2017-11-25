from lib import name


def handle(event, context):
    supplied_name = event['queryStringParameters'].get('name', None)
    message_name = name.display_name(supplied_name)
    message = 'Hello {}'.format(message_name)
    return {'message': message}
