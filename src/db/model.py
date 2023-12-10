from typing import List, Optional

from pydantic import BaseModel


class BookShort(BaseModel):
    """Модель Книга."""

    title: str


class AuthorShort(BaseModel):
    """Модель Автор."""

    name: str
    country: Optional[str]
    books: List[BookShort]


class Book(BookShort):
    """Модель Книга расширенная."""

    id: Optional[int]
    author_id: Optional[int]

    @classmethod
    def create(cls, row: tuple):
        """Создание объекта модели Книга."""
        return cls(id=row[0], title=row[1], author_id=row[2])


class Author(AuthorShort):
    """Модель Автор расширенная."""

    id: Optional[int]
    books: List[Book]

    @classmethod
    def create(cls, row: tuple, books: List[Book]):
        """Создание объекта модели Автор."""
        return cls(id=row[0], name=row[1], country=row[2], books=books)


class AuthorResponse(BaseModel):
    """Модель Авторы и книги."""

    authors: List[Author]
