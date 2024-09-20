from fastapi import FastAPI

from src.products.routes import router as product_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов API
    """

    app.include_router(product_router)

    return app
