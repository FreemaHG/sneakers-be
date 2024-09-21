from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.products.models.favourite import FavouriteProduct
from src.products.repositories.favourite import FavouriteRepository
from src.products.repositories.product import ProductRepository
from src.products.schemas.favourite import FavouriteAddSchema


class FavouriteService:
    """
    Вывод избранных товаров
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> list[FavouriteProduct] | None:
        """
        Возврат списка избранных товаров
        :param session: объект асинхронной сессии
        :return: список с товарами
        """

        products = await FavouriteRepository.get_list(session=session)
        return products

    @classmethod
    async def add_product(cls, new_product: FavouriteAddSchema, session: AsyncSession) -> FavouriteProduct:
        """
        Добавление товара в избранное
        :param new_product: новый товар
        :param session: объект асинхронной сессии
        :return: новая запись о товаре в избранном
        """
        product = await ProductRepository.get(product_id=new_product.id, session=session)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Товар не найден'
            )

        res = await FavouriteRepository.get(product_id=new_product.id, session=session)

        if res:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='Товар уже в избранном'
            )

        record = await FavouriteRepository.add_product(product=product, session=session)

        return record


    @classmethod
    async def delete_product(cls, product_id: int, session: AsyncSession) -> None:
        """
        Удаление товара из избранного
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: None
        """
        record = await FavouriteRepository.get(product_id=product_id, session=session)

        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Товар не найден в избранном'
            )

        await FavouriteRepository.delete(record=record, session=session)
