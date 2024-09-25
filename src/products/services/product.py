from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models.product import Product
from src.products.repositories.product import ProductRepository


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

        products = await ProductRepository.get_list(
            title=title,
            limit=limit,
            offset=offset,
            session=session
        )
        return products

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Product | None:
        """
        Возврат товара по id
        :param product_id: id товара
        :param session: объект асинхронной сессии
        :return: объект товара
        """

        post = await ProductRepository.get(product_id=product_id, session=session)
        return post
