from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.cart.models import Cart
from src.cart.repositories import CartRepository
from src.cart.schemas import CartAddSchema
from src.products.models.product import Product
from src.products.repositories.product import ProductRepository


class CartService:
    """
    Возврат товаров в корзине
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> list[Product] | None:
        """
        Возврат товаров в корзине
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        records = await CartRepository.get_list(session=session)

        return records

    @classmethod
    async def add_product(cls, new_product: CartAddSchema, session: AsyncSession) -> Cart:
        """
        Добавление товара в корзину
        :param new_product: новый товар
        :param session: объект асинхронной сессии
        :return: новая запись о товаре в корзине
        """
        product = await ProductRepository.get(product_id=new_product.id, session=session)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Товар не найден'
            )

        record = await CartRepository.add_product(product=product , count=new_product.count, session=session)

        return record

    @classmethod
    async def delete_product(cls, product_id: int, session: AsyncSession) -> None:
        """
        Удаление товара из корзины
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: None
        """
        record = await CartRepository.get(product_id=product_id, session=session)

        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Товар в корзине не найден'
            )

        await CartRepository.delete(record=record, session=session)
