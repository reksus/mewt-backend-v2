from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
# from app_config import settings

# DATABASE_URL = settings.DATABASE_URL

# setup sync session class
SYNC_DATABASE_URL = "postgresql+psycopg2://testuser:admin@localhost:5432/hello_db"
sync_engine = create_engine(SYNC_DATABASE_URL)
sync_session = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

# setup async session class
ASYNC_DATABASE_URL = "postgresql+asyncpg://testuser:admin@localhost:5432/hello_db"
async_engine = create_async_engine(ASYNC_DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)



Base = declarative_base()
