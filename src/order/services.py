from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.cart.repositories import CartRepository
from src.order.models import Order
from src.order.repositories import OrderRepository
from src.products.repositories.product import ProductRepository


class OrderService:
    """
    Создание и возврат данных о заказах
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> list[Order] | None:
        """
        Возврат данных о заказах
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        orders = await OrderRepository.get_list(session=session)

        return orders

    @classmethod
    async def create(cls, products_ids: list[int], session: AsyncSession) -> Order:
        """
        Создание заказа
        :param products_ids: список с идентификаторами товаров
        :param session: объект асинхронной сессии
        :return: новая запись о заказе
        """

        cart_products = await CartRepository.get_list(products_ids=products_ids, session=session)

        found_ids = [record.product_id for record in cart_products]
        not_found_ids = [prod_id for prod_id in products_ids if prod_id not in found_ids]

        if not_found_ids:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Не найдены товары в корзине со следующими идентификаторами: {not_found_ids}'
            )

        products = await ProductRepository.get_list(ids_list=products_ids, session=session)

        order = await OrderRepository.create(products=products, session=session)
        await CartRepository.clear(products_ids=products_ids, session=session)

        return order
