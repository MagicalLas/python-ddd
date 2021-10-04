from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List


class Category(Enum):
    HISTORY = auto
    MATH = auto
    COMPUTER = auto
    HUMANITY = auto

    @staticmethod
    def get_category_from_str(category_text: str) -> Category:
        return Category.MATH


@dataclass
class Code(object):
    book_category: Category
    number: int

    def __init__(self, raw_code: str):
        self.number = int(raw_code.split(":")[1])
        self.book_category = Category.get_category_from_str(raw_code.split(":")[0])


class Book(object):
    def __init__(self, title: str, book_code: Code, rental_list_id: int):
        self._title = title
        self._code = book_code
        self._rental_list_id = rental_list_id


class BookRepository(object):
    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def save(self, book: Book):
        pass

    @abstractmethod
    def find_by_title(self, book_title: str) -> List[Book]:
        pass
