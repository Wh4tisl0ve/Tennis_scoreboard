from app.mini_framework import app


class Pagination:
    def __init__(self, items: list, items_per_page: int = 10, current_page: int = 1):
        self.__items = items
        self.__items_per_page = items_per_page
        self.__current_page = current_page
        self.__total_record = len(items)

    @property
    def links(self) -> str:
        pagination = {'items_per_page': self.__items_per_page,
                      'total_record': self.__total_record,
                      'current_page': self.__current_page}

        return app.render_template('pagination.html',
                                   data=pagination)
