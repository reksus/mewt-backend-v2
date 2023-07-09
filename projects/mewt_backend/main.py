from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .src.config import settings
from .src.routers.api import router as router_api
from .src.internal import admin
import uvicorn


def get_application() -> FastAPI:
    ''' Configure, start and return the application '''
    
    ## Start FastApi App 
    application = FastAPI()

    ## Mapping api routes
    application.include_router(router_api, prefix=settings.API_PREFIX)
    
    ## Add exception handlers
    # application.add_exception_handler(HTTPException, http_error_handler)

    ## Allow cors
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ## Example of admin route
    # application.include_router(
    #     admin.router,
    #     prefix="/admin",
    #     tags=["admin"],
    #     dependencies=[Depends(get_token_header)],
    #     responses={418: {"description": "I'm a teapot"}},
    # )

    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run("mewt_backend.main:app", port=1111, host='127.0.0.1')

