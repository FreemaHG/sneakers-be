from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models import Product
from src.products.repositories import ProductRepository


class ProductService:
    """
    Вывод товаров
    """

    @classmethod
    async def get_list(
            cls, session: AsyncSession, title: str = None, limit: int = None, offset: int = None
    ) -> list[Product] | None:
        """
        Возврат списка товаров
        :param title: название товара
        :param limit: кол-во возвращаемых записей
        :param offset: сдвиг в наборе результатов
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        # TODO Возврат из кэша если есть

        products = await ProductRepository.get_list(
            title=title,
            limit=limit,
            offset=offset,
            session=session
        )

        # TODO Добавить кэширование

        return products

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Product | None:
        """
        Возврат товара по id
        :param product_id: id товара
        :param session: объект асинхронной сессии
        :return: объект товара
        """
        # TODO Возврат из кэша если есть

        post = await ProductRepository.get(product_id=product_id, session=session)

        # TODO Добавить кэширование

        return post
