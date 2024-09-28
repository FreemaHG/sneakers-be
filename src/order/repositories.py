from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from src.order.models import Order
from src.products.models.product import Product


class OrderRepository:
    """
    Возврат и создание заказов
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> list[Order]:
        """
        Возврат заказов
        :param session: объект асинхронной сессии
        :return: список с заказами
        """

        query = select(Order)
        orders = await session.execute(query)

        return orders.unique().scalars().all()


    @classmethod
    async def create(cls, products: list[Product], session: AsyncSession) -> Order | None:
        """
        Создание заказа с товарами
        :param products: товары для добавления в заказ
        :param session: объект асинхронной сессии
        :return: новая запись о заказе
        """

        order = Order(products=products)
        session.add(order)
        await session.commit()

        return order
