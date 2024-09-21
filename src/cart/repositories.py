from typing import List

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.models import Cart
from src.products.models import Product


class CartRepository:
    """
    Возврат, добавление и удаление товаров из корзины
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> List[Cart]:
        """
        Возврат товаров в корзине
        :param session: объект асинхронной сессии
        :return: список с товарами
        """

        query = select(Cart)
        products = await session.execute(query)

        return products.scalars()

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Cart | None:
        """
        Возврат записи о товаре в корзине по id товара
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: объект записи о товаре
        """
        query = select(Cart).where(Cart.product_id == product_id)
        record = await session.execute(query)

        return record.scalar_one_or_none()


    @classmethod
    async def add_product(cls, product: Product, count: int, session: AsyncSession) -> Cart | None:
        """
        Добавление товара в корзину
        :param product: объект товара
        :param count: кол-во товара
        :param session: объект асинхронной сессии
        :return: новая запись о добавленном товаре
        """

        record = Cart(product=product, count=count)
        session.add(record)
        await session.commit()

        return record

    @classmethod
    async def delete(cls, record: Cart, session: AsyncSession) -> None:
        """
        Удаление товара из корзины
        :param record: запись о товаре в корзине для удаления
        :param session: объект асинхронной сессии
        :return: None
        """

        await session.delete(record)
        await session.commit()
