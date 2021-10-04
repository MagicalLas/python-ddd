from bookmanagement.domain.book import BookRepository, Book, Code
from bookmanagement.domain.rental_list import RentalList


class BookManagementUseCase(object):
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def create_new_book(self, title: str, raw_code: str):
        rental_list = RentalList()
        book = Book(title, Code(raw_code), [])
        self._book_repository
