from .database import async_session, sync_session


# sync db session 
def get_sync_session():
    with sync_session() as session:
        try:
            with session.begin():
                yield session
        except: 
            session.rollback()
        finally:
            session.close()
    
# async db session 
async def get_async_session():
    async with async_session() as session:
        try:
            async with session.begin():
                yield session
        except: 
            await session.rollback()
        finally:
            await session.close()