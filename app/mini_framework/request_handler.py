from urllib.parse import parse_qs

from app.exceptions import NotFoundError
from app.mini_framework import app


def handle_request(environ, start_response):
    try:
        request_method = environ['REQUEST_METHOD']
        request_uri = environ['REQUEST_URI']
        query_params = parse_qs(environ['QUERY_STRING'])

        print(f'Method: {request_method}, params: {query_params}, uri: {request_uri}')

        handler = app.get_handlers(request_uri, request_method)

        query_params = unpack_dict_values(query_params)
        query_params['input_data'] = unpack_dict_values(parse_qs(environ['wsgi.input'].read().decode('utf-8')))
        query_params['method'] = request_method

        response = handler(query_params, start_response)
        return [response.encode()]
    except NotFoundError as error:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [app.render_template('error.html', data=error).encode()]


def unpack_dict_values(params: dict) -> dict:
    return {k: v[0] for k, v in params.items()}
