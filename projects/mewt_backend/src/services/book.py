
from typing import List, Optional, Any, Awaitable

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from ..models import Book

def get_all_books(sync_session) -> List[Book]:
    q = sync_session.execute(select(Book).order_by(Book.id))
    return q.scalars().all()


async def get_all_books_async(async_session) -> List[Book]:
    q = await async_session.execute(select(Book).order_by(Book.id))
    return q.scalars().all()

async def create_book(name: str, author: str, release_year: int, async_session) -> None:
    new_book = Book(name=name,author=author, release_year=release_year)
    async_session.add(new_book)
    await async_session.flush()