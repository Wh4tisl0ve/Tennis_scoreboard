from urllib.parse import parse_qs

from app.mini_framework import app


def handle_request(environ, start_response):
    request_method = environ['REQUEST_METHOD']
    request_uri = environ['REQUEST_URI']
    query_params = parse_qs(environ['QUERY_STRING'])

    print(f'Method: {request_method}, params: {query_params}, uri: {request_uri}')

    handler = app.get_handlers(request_uri, request_method)

    query_params = {k: v[0] for k, v in query_params.items()}
    query_params['input_data'] = parse_qs(environ['wsgi.input'].read().decode('utf-8'))
    query_params['method'] = request_method

    response = handler(query_params, start_response)
    return [response.encode()]

