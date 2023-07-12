from fastapi import APIRouter, Depends
from ..dependencies import get_async_session, get_sync_session
from sqlalchemy.orm import Session


router = APIRouter()


from ..services import book


@router.get("/books/sync")
async def get_all_books(sync_session: Session = Depends(get_sync_session)):
    return book.get_all_books(sync_session)


@router.get("/books")
async def get_all_books(async_session: Session = Depends(get_async_session)):
    return await book.get_all_books_async(async_session)

@router.post("/books")
async def create_book(name: str, author: str, release_year: int, async_session: Session = Depends(get_async_session)):
    return await book.create_book(name, author, release_year, async_session)


