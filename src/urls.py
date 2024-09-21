from fastapi import FastAPI

from src.products.routes.product import router as product_router
from src.products.routes.favourite import router as favourite_router
from src.cart.routes import router as cart_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов API
    """
    app.include_router(product_router)
    app.include_router(favourite_router)
    app.include_router(cart_router)

    return app
