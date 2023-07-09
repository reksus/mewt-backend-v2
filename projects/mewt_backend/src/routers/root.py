from fastapi import APIRouter, Depends
from ..dependencies import get_async_session
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/root")
def root():
    return {"data": "hello world!!!"}