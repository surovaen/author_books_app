from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection

from core.repository import AbstractRepository
from db.model import Author, AuthorShort, Book, BookShort


class AuthorRepository(AbstractRepository):
    """Репозиторий для сущности Автор."""

    def __init__(self, conn: AsyncConnection):
        """Инициализация подключения."""
        self.conn = conn

    async def get(self, author_id: int):
        """Метод получения записи по id."""
        statement = """SELECT id, name FROM author WHERE id = :author_id"""
        result = await self.conn.execute(
            text(statement),
            {'author_id': author_id},
        )
        return result.one_or_none()

    async def list(self):
        """Метод получения всех записей из БД."""
        statement = """SELECT * FROM author ORDER BY name"""
        result = await self.conn.execute(text(statement))
        return result.all()

    async def add(self, author: AuthorShort):
        """Метод добавления записи в БД."""
        statement = """INSERT INTO author(name, country) VALUES (:name, :country) RETURNING id"""
        result = await self.conn.execute(
            text(statement),
            {'name': author.name, 'country': author.country},
        )
        return result.scalar_one_or_none()

    async def update(self, author: Author):
        """Метод обновления записи в БД."""
        statement = """UPDATE author SET name = :name, country = :country WHERE id = :id"""
        await self.conn.execute(
            text(statement),
            {'name': author.name, 'country': author.country, 'id': author.id},
        )

    async def delete(self, author_id: int):
        """Метод удаления записи из БД."""
        statement = """DELETE FROM author WHERE id = :id"""
        await self.conn.execute(
            text(statement),
            {'id': author_id},
        )

    async def filter(self, limit: int = None, author_name: str = None, country: str = None):
        """Метод получения отфильтрованных записей из БД."""
        statement = """SELECT * FROM author"""
        params = dict()
        name_statement = ''
        country_statement = ''

        if author_name:
            name_statement = """ name ILIKE :name"""
            params['name'] = '%{}%'.format(author_name)

        if country:
            country_statement = """ country ILIKE :country"""
            params['country'] = '%{}%'.format(country)

        if name_statement or country_statement:
            statement += """ WHERE"""
            if name_statement and country_statement:
                statement += name_statement + """ AND """ + country_statement
            else:
                statement += name_statement if name_statement else country_statement

        statement += """ ORDER BY name"""

        result = await self.conn.execute(
            text(statement),
            parameters=params,
        )

        if limit:
            return result.all()[:limit]

        return result.all()


class BookRepository(AbstractRepository):
    """Репозиторий для сущности Книга."""

    def __init__(self, conn: AsyncConnection):
        """Инициализация подключения."""
        self.conn = conn

    async def get(self, book_id: int):
        """Метод получения записи по id."""
        statement = """SELECT * FROM book WHERE id = :id"""
        result = await self.conn.execute(
            text(statement),
            {'id': book_id},
        )
        return result.one_or_none()

    async def add(self, book: BookShort, author_id: int):
        """Метод добавления записи в БД."""
        statement = """INSERT INTO book(title, author_id) VALUES (:title, :author_id)"""
        await self.conn.execute(
            text(statement),
            {'title': book.title, 'author_id': author_id},
        )

    async def update(self, book: Book):
        """Метод обновления записи в БД."""
        statement = """UPDATE book SET title = :title WHERE id = :id"""
        await self.conn.execute(
            text(statement),
            {'title': book.title, 'id': book.id},
        )

    async def delete(self, book_id: int):
        """Метод удаления записи из БД."""
        statement = """DELETE FROM book WHERE id = :id"""
        await self.conn.execute(
            text(statement),
            {'id': book_id},
        )

    async def list(self):
        """Метод получения всех записей из БД."""
        statement = """SELECT * FROM book ORDER BY title"""
        result = await self.conn.execute(text(statement))
        return result.all()

    async def filter(self, author_id: int):
        """Метод получения отфильтрованных записей из БД."""
        statement = """SELECT * FROM book WHERE author_id = :author_id ORDER BY title"""
        result = await self.conn.execute(
            text(statement),
            {'author_id': author_id},
        )
        return result.all()
