from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse, Response

from database import engine
from db.model import Author, AuthorResponse, AuthorShort, Book
from db.repository import AuthorRepository, BookRepository


router = APIRouter()


@router.get(
    '/author',
    summary='GET запрос всех авторов и их книг',
    status_code=status.HTTP_200_OK,
)
async def get_authors(
        limit: int = None,
        author_name: str = None,
        country: str = None,
):
    """Эндпоинт получения списка всех авторов и их книг.

    Параметры фильтрации:
    limit - количество возвращаемых записей;
    author_name - имя автора;
    country - страна автора.
    """
    response = AuthorResponse(authors=[])

    async with engine.connect() as conn:
        async with conn.begin():
            if limit or author_name or country:
                authors_db_result = await AuthorRepository(conn).filter(limit, author_name, country)
            else:
                authors_db_result = await AuthorRepository(conn).list()

            for a_row in authors_db_result:
                books_db_result = await BookRepository(conn).filter(a_row[0])
                books = [Book.create(row=b_row) for b_row in books_db_result]
                response.authors.append(
                    Author.create(
                        row=a_row,
                        books=books,
                    ),
                )

    return JSONResponse(
        content=response.model_dump(exclude_none=True),
    )


@router.post(
    '/author',
    summary='POST запрос на создание автора и его книг',
    status_code=status.HTTP_201_CREATED,
)
async def add_author(author: AuthorShort):
    """Эндпоинт создания автора и его книг."""
    async with engine.connect() as conn:
        async with conn.begin():
            author_id = await AuthorRepository(conn).add(author)

            for book in author.books:
                await BookRepository(conn).add(book, author_id)

    return Response()


@router.put(
    '/author',
    summary='PUT запрос на обновление данных автора и его книг',
    status_code=status.HTTP_200_OK,
)
async def update_author(author: Author):
    """Эндпоинт обновления данных автора и его книг."""
    async with engine.connect() as conn:
        async with conn.begin():
            await AuthorRepository(conn).update(author)

            for book in author.books:
                if book.id:
                    await BookRepository(conn).update(book)
                else:
                    await BookRepository(conn).add(book, author.id)
    return Response()


@router.delete(
    '/author',
    summary='DELETE запрос на удаление автора и его книг',
    status_code=status.HTTP_200_OK,
)
async def delete_author(author_id: int):
    """Эндпоинт удаления автора и его книг по id автора."""
    async with engine.connect() as conn:
        async with conn.begin():
            await AuthorRepository(conn).delete(author_id)

    return Response()


@router.delete(
    '/book',
    summary='DELETE запрос на удаление книги',
    status_code=status.HTTP_200_OK,
)
async def delete_book(book_id: int):
    """Эндпоинт удаления книги по id книги."""
    async with engine.connect() as conn:
        async with conn.begin():
            await BookRepository(conn).delete(book_id)

    return Response()
