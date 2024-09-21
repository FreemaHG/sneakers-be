from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models.favourite import FavouriteProduct
from src.products.models.product import Product


class FavouriteRepository:
    """
    Возврат, добавление и удаление товаров из избранного
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> List[FavouriteProduct]:
        """
        Возврат избранных товаров
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        query = select(FavouriteProduct)
        products = await session.execute(query)

        return products.scalars()

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> FavouriteProduct | None:
        """
        Возврат записи об избранном товаре по id товара
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: объект записи о товаре
        """
        query = select(FavouriteProduct).where(FavouriteProduct.product_id == product_id)
        record = await session.execute(query)

        return record.scalar_one_or_none()

    @classmethod
    async def add_product(cls, product: Product, session: AsyncSession) -> FavouriteProduct | None:
        """
        Добавление товара в избранное
        :param product: объект товара
        :param session: объект асинхронной сессии
        :return: новая запись об избранном товаре
        """

        record = FavouriteProduct(product=product)
        session.add(record)
        await session.commit()

        return record

    @classmethod
    async def delete(cls, record: FavouriteProduct, session: AsyncSession) -> None:
        """
        Удаление товара из избранного
        :param record: запись об избранном товаре для удаления
        :param session: объект асинхронной сессии
        :return: None
        """

        await session.delete(record)
        await session.commit()
