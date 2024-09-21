from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models import Product


class ProductRepository:
    """
    Возврат товаров
    """

    @classmethod
    async def get_list(
            cls, session: AsyncSession, title: str = None, limit: int = None, offset: int = None
    ) -> List[Product]:
        """
        Фильтрация и возврат товаров
        :param title: название товара
        :param limit: кол-во возвращаемых записей
        :param offset: сдвиг в наборе результатов
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        query = select(Product)

        if title:
            query = query.where(Product.title.ilike(f'%{title}%'))

        if limit is not None and offset is not None:
            query = query.limit(limit).offset(offset)

        products = await session.execute(query)

        return products.scalars()

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Product | None:
        """
        Возврат товара по id
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: объект товара | None
        """
        query = select(Product).where(Product.id == product_id)
        product = await session.execute(query)

        return product.scalar_one_or_none()
