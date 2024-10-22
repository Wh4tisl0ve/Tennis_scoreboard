import re
from typing import Callable

from jinja2 import Environment, FileSystemLoader

from app.exceptions import NotFoundError


class MiniFrameWork:
    def __init__(self):
        self.__routes: dict = {'GET': {}, 'POST': {}}

    def route(self, url: str, methods: list):
        def register_route(handler: Callable):
            for method in methods:
                self.__routes[method][re.compile(url)] = handler

        return register_route

    def get_handlers(self, url: str, method: str = 'GET') -> list[Callable]:
        for endpoint, handler in self.__routes[method].items():
            if endpoint.match(url):
                return handler

        raise NotFoundError("Endpoint не найден")

    def render_template(self, *args, **kwargs) -> str:
        file_loader = FileSystemLoader('app/templates')
        env = Environment(loader=file_loader)

        template = env.get_template(args[0])
        rendered_template = template.render(data=kwargs.get('data'),
                                            pagination=kwargs.get('pagination'),
                                            filters=kwargs.get('filters'))

        return rendered_template
