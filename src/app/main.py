from waitress import serve


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, Wodfrld!']


def run_server(host='127.0.0.1', port='5000'):
    print(f'Server running on port {port}')
    serve(hello_world, listen=f'{host}:{port}')


if __name__ == '__main__':
    run_server()
