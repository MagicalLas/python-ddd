from __future__ import annotations

from typing import List, Optional, Iterable

from django.db import models

from domain.book import BookRepository, Book, Code
from domain.rental_list import RentalList


class DjangoModelOfBook(models.Model):
    title = models.TextField
    code = models.TextField
    rental_list_id = models.TextField

    @staticmethod
    def to_domain(book_data: DjangoModelOfBook) -> Book:
        rental_list_data: DjangoModelOfRentalList = DjangoModelOfRentalList.objects.get(book_data.rental_list_id)
        return Book(
            title=str(book_data.title),
            book_code=Code(str(book_data.code)),
            rental_list=DjangoModelOfRentalList.to_domain(rental_list_data),
        )


class DjangoModelOfRentalList(models.Model):
    id = models.TextField
    data = models.TextField

    @staticmethod
    def to_domain(rental_list_data: DjangoModelOfRentalList) -> RentalList:
        return RentalList(
            rental_list_id=rental_list_data.id,
            # skip some implementation for readability and effort.
        )


class DjangoBookRepository(BookRepository):
    def find_by_id(self, book_id: int) -> Optional[Book]:
        try:
            book_data: DjangoModelOfBook = DjangoModelOfBook.objects.get(pk=book_id)
            return DjangoModelOfBook.to_domain(book_data)
        except Exception as e:
            print(e)
            return None

    def save(self, book: Book):
        book_data: DjangoModelOfBook = DjangoModelOfBook.objects.get(pk=book.id)
        book_data.code = book.code
        book_data.rental_list_id = book.rental_list
        book_data.save()

    def find_by_title(self, book_title: str) -> List[Book]:
        books_data: Iterable[DjangoModelOfBook] = DjangoModelOfBook.objects.filter(title=book_title)
        return [DjangoModelOfBook.to_domain(book_data) for book_data in books_data]
