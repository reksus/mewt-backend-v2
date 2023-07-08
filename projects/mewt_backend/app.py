from fastapi import FastAPI
import uvicorn

app = FastAPI()

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
# from app_config import settings

# DATABASE_URL = settings.DATABASE_URL
DATABASE_URL = "postgresql+asyncpg://testuser:admin@localhost:5432/hello_db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

from sqlalchemy import Column, Integer, String

# from db.config import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)


@app.get("/")
def root():
    return {"data": "hello world!!!"}


if __name__ == '__main__':
    uvicorn.run("mewt_backend.app:app", port=1111, host='127.0.0.1')

