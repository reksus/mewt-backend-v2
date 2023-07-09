from .database import async_session


async def get_async_session():
    async with async_session() as session:
        try:
            async with session.begin():
                yield session
        except: 
            await session.rollback()
        finally:
            await session.close()