from math import ceil

from app.mini_framework import app


class Pagination:
    def __init__(self, total_records: int, items_per_page: int = 10, current_page: int = 1):
        self.__total_records = total_records
        self.__items_per_page = items_per_page
        self.__current_page = current_page
        self.__total_pages = ceil(total_records / items_per_page)

    @property
    def links(self) -> str:
        pagination_config = {'items_per_page': self.__items_per_page,
                             'total_pages': self.__total_pages,
                             'current_page': self.__current_page}

        return app.render_template('pagination.html',
                                   data=pagination_config)

    @property
    def info(self) -> str:
        return f'<div>Found {self.__total_records} records, page {self.__current_page}-{self.__total_pages}</div>'
