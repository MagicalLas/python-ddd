from fastapi import FastAPI

from adapter.bookrepository import DjangoBookRepository
from application.bookmanagement import BookManagementUseCase

app = FastAPI()

book_repository = DjangoBookRepository()
book_management_use_case = BookManagementUseCase(book_repository)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/books")
def read_item():
    # skip some implementation details
    book_management_use_case.create_new_book("title", "raw_code")


@app.get("/books/{title}")
def read_item(title: str):
    # skip some implementation details
    return book_management_use_case.find_book_from_title(title)
