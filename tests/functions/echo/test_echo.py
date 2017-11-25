import json

from functions.echo import echo


def test_when_the_name_is_supplied():
    event = {
        'queryStringParameters': {
            'name': 'robert'
        }
    }
    response = echo.handle(event, {})
    assert(parse_body(response['body'])['message'] == 'Hello robert')


def test_when_the_name_is_not_supplied():
    event = {
        'queryStringParameters': None
    }
    response = echo.handle(event, {})
    assert (parse_body(response['body'])['message'] == 'Hello there')


def parse_body(body):
    return json.loads(body)
