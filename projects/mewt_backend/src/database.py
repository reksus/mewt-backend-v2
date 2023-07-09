from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
# from app_config import settings

# DATABASE_URL = settings.DATABASE_URL
DATABASE_URL = "postgresql+asyncpg://testuser:admin@localhost:5432/hello_db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
