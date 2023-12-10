from sqlalchemy import Column, ForeignKey, Integer, String, Table

from database import metadata


author = Table(
    'author',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(150), nullable=False),
    Column('country', String(150), nullable=True),
)

book = Table(
    'book',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(150), nullable=False),
    Column('author_id', Integer, ForeignKey(author.c.id, ondelete='CASCADE'), nullable=False),
)
