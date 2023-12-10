from model import Author, Book
from sqlalchemy.orm import registry, relationship
from table import author, book


mapper_registry = registry()

mapper_registry.map_imperatively(
    Author,
    author,
    properties={
        "addresses": relationship(Book, backref='author', order_by=author.c.id)
    },
)

mapper_registry.map_imperatively(Book, book)
