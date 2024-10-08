from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.models import Cart
from src.products.models.product import Product


class CartRepository:
    """
    Возврат, добавление и удаление товаров из корзины
    """

    @classmethod
    async def get_list(cls, session: AsyncSession, products_ids: list[int] = None) -> list[Cart]:
        """
        Возврат товаров в корзине
        :param products_ids: список с идентификаторами товаров в корзине
        :param session: объект асинхронной сессии
        :return: список с товарами
        """

        query = select(Cart)

        if products_ids:
            query = query.where(Cart.product_id.in_(products_ids))

        products = await session.execute(query)

        return products.scalars().all()

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
    async def add_product(cls, product: Product, session: AsyncSession) -> Cart | None:
        """
        Добавление товара в корзину
        :param product: объект товара
        :param session: объект асинхронной сессии
        :return: новая запись о добавленном товаре
        """

        record = Cart(product=product)
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

    @classmethod
    async def clear(cls, products_ids: list[int], session: AsyncSession) -> None:
        """
        Учистка корзины через удаление всех записей, где встречаются товары с переданными id
        :param products_ids: список с идентификаторами товаров
        :param session: объект асинхронной сессии
        :return: None
        """

        query = delete(Cart).where(Cart.product_id.in_(products_ids))
        await session.execute(query)
        await session.commit()
