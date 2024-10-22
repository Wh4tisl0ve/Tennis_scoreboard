import urllib.parse
from math import ceil

from app.mini_framework import app


class Pagination:
    def __init__(self, total_records: int, filters: dict, items_per_page: int = 10, current_page: int = 1):
        self.__total_records = total_records
        self.__items_per_page = items_per_page
        self.__current_page = current_page
        self.__total_pages = ceil(total_records / items_per_page)
        self.__filters = filters

    @property
    def query_string_filters(self) -> str:
        params = {k: v for k, v in self.__filters.items() if v}
        query_string = urllib.parse.urlencode(params)
        return '&' + query_string if query_string else ''

    @property
    def links(self) -> str:
        pagination_config = {'items_per_page': self.__items_per_page,
                             'total_pages': self.__total_pages,
                             'current_page': self.__current_page}

        return app.render_template('includes/pagination.html',
                                   data=pagination_config,
                                   filters=self.query_string_filters)

    @property
    def info(self) -> str:
        return f'<div>Found {self.__total_records} records, page {self.__current_page}-{self.__total_pages}</div>'
