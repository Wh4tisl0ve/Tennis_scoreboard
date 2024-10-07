import re
from typing import Callable

from jinja2 import Environment, FileSystemLoader


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

        raise Exception("Endpoint не найден")

    def render_template(self, template_name: str, data=None) -> str:
        file_loader = FileSystemLoader('src/app/templates')
        env = Environment(loader=file_loader)

        template = env.get_template(template_name)

        rendered_template = template.render()

        print(rendered_template)

        return rendered_template