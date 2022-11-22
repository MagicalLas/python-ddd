from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List

from domain.rental_list import RentalList


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

    def __str__(self):
        return f"{self.book_category}:{self.number}"


class Book(object):
    def __init__(self, title: str, book_code: Code, rental_list: RentalList):
        self._title = title
        self._code = book_code
        self._rental_list = rental_list

    @staticmethod
    def create(title: str, book_code: Code) -> Book:
        return Book(title, book_code, RentalList.create())

    @property
    def code(self) -> str:
        return str(self._code)

    @property
    def title(self) -> str:
        return self._title

    @property
    def rental_list(self) -> List[str]:
        return [record.user_id for record in self._rental_list.records]

    @property
    def id(self):
        return self.code


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
