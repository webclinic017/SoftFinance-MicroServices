from fastapi import FastAPI
from .infrastructure.connection import create_tables


__version__ = '1.0'


def create_app(title: str, description: str) -> FastAPI:
    app = FastAPI(title=title, description=description)

    app = include_routers(app) 
    app = init_db(app)

    return app

def include_routers(app: FastAPI) -> FastAPI:
    from .controllers import user_controller, auth_controller

    app.include_router(user_controller.router)
    app.include_router(auth_controller.router)
    return app

def init_db(app: FastAPI) -> FastAPI:
    
    @app.on_event('startup')
    def startup():
        create_tables()
    
    return app
