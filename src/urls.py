from fastapi import FastAPI


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов API
    """
    # app.include_router(category_router)

    return app
