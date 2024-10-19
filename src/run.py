from waitress import serve
from whitenoise import WhiteNoise
from app.config import settings

from app.mini_framework.request_handler import handle_request


def run_server(request_handler=handle_request, host=settings.run.host, port=settings.run.port) -> None:
    print(f'Server running on http://{host}:{port}')
    app = WhiteNoise(request_handler)
    app.add_files('src/app/static/', prefix='static/')
    serve(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
