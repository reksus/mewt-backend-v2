from fastapi import APIRouter

from ..config import settings

from . import book, root

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    # router.include_router(auth.router)
    router.include_router(root.router, prefix=settings.ROUTE_PREFIX_V1)
    router.include_router(book.router, prefix=settings.ROUTE_PREFIX_V1)

include_api_routes()