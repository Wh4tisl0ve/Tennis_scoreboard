import re
from typing import Callable


class Router:
    def __init__(self):
        self.__routes: dict = {'GET': {}, 'POST': {}}

    def route(self, url: str, methods: list):
        def register_route(handler: Callable) -> list[Callable]:
            handlers = []
            for method in methods:
                handlers.append(handler)
                self.__routes[method][re.compile(url)] = handler
            return handlers

        return register_route

    def get_handler(self, url: str, method: str = 'GET'):
        for endpoint, handler in self.__routes[method].items():
            if endpoint.match(url):
                return handler

        raise Exception("Enpoint не найден")
