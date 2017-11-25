from functions.echo import echo


def test_when_the_name_is_supplied():
    event = {
        'queryStringParameters': {
            'name': 'robert'
        }
    }
    response = echo.handle(event, {})
    assert(response['message'] == 'Hello robert')


def test_when_the_name_is_not_supplied():
    event = {
        'queryStringParameters': {}
    }
    response = echo.handle(event, {})
    assert (response['message'] == 'Hello there')
