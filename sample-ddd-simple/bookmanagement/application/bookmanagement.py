from domain.book import BookRepository, Book, Code


class BookManagementUseCase(object):
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def create_new_book(self, title: str, raw_code: str):
        book = Book.create(title, Code(raw_code))
        self._book_repository.save(book)

    def find_book_from_title(self, title: str):
        books = self._book_repository.find_by_title(title)
        return books
