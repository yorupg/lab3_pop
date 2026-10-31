from src.errors import DuplicateIdError, InvalidBookError
from src.model import Book


class Catalog:
    def __init__(self):
        self._items = {}

    def add(self, item):
        if not isinstance(item, Book):
            raise InvalidBookError

        if item.item_id in self._items:
            raise DuplicateIdError

        self._items[item.item_id] = item

    def get(self, item_id):

        self[item_id] = self.get(item_id, 0)
