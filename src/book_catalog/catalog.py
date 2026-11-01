from book_catalog.errors import DuplicateIdError, InvalidBookError, BookNotFounderError
from book_catalog.model import Book


class Catalog:
    def __init__(self) -> None:
        self._items: dict[str, Book] = {}

    def add(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise InvalidBookError

        if item.item_id in self._items:
            raise DuplicateIdError

        self._items[item.item_id] = item

    def get(self, item_id: str) -> Book:
        if item_id in self._items:
            return self._items[item_id]
        raise BookNotFounderError

    def remove(self, item_id: str) -> None:
        if item_id in self._items:
            del self._items[item_id]
        else:
            raise BookNotFounderError

    def find_by_category(self, category: str) -> list[Book]:
        res = []
        for book in self._items.values():
            if book.category == category:
                res.append(book)

        return res

    def find_by_name(self, name: str) -> list[Book]:
        res = []
        for book in self._items.values():
            if name.lower() in book.name.lower():
                res.append(book)

        return res

    def __len__(self) -> int:
        return len(self._items)

    #def __iter__():


    def __contains__(self, item_id: str) -> bool:
        return item_id in self._items
