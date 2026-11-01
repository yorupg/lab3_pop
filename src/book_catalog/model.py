from dataclasses import dataclass

from book_catalog.errors import InvalidBookError


@dataclass
class Book:
    item_id: str
    name: str
    author: str
    category: str
    year: int
    pages: int

    def __post_init__(self):

        if isinstance(self.pages, int):
            if self.pages <= 0:
                raise InvalidBookError
        else:
            raise InvalidBookError

        if isinstance(self.year, int):
            if self. year <= 0:
                raise InvalidBookError
        else:
            raise InvalidBookError

        if isinstance(self.item_id, str):
            if self.item_id.strip() == "":
                raise InvalidBookError
        else:
            raise InvalidBookError

        if isinstance(self.name, str):
            if self.name.strip() == "":
                raise InvalidBookError
        else:
            raise InvalidBookError

        if isinstance(self.author, str):
            if self.author.strip() == "":
                raise InvalidBookError
        else:
            raise InvalidBookError

        if isinstance(self.category, str):
            if self.category.strip() == "":
                raise InvalidBookError
        else:
            raise InvalidBookError
