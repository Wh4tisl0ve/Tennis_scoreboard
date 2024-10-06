from urllib.parse import parse_qs

from app.mini_framework import router


def handle_request(environ, start_response):
    request_method = environ['REQUEST_METHOD']
    request_uri = environ['REQUEST_URI']
    query_params = parse_qs(environ['QUERY_STRING'])
    print(f'Method: {request_method}, params: {query_params}, uri: {request_uri}')

    handler = router.get_handler(request_uri, request_method)

    query_params = {k: v[0] for k, v in query_params.items()}
    response = handler(query_params)

    send_response('200 OK', start_response)

    return [response.encode()]


def send_response(status: str, start_response):
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
