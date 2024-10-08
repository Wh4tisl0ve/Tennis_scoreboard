from waitress import serve
from whitenoise import WhiteNoise

from app.mini_framework.request_handler import handle_request


def run_server(request_handler=handle_request, host="localhost", port=8080) -> None:
    print(f'Server running on http://{host}:{port}')
    app = WhiteNoise(request_handler)
    app.add_files('src/app/static/', prefix='static/')
    serve(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
