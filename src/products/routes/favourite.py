from typing import List, Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_async_session
from src.products.schemas.favourite import FavouriteProductSchema, FavouriteAddSchema
from src.products.services.favourite import FavouriteService
from src.router import BaseRouter
from src.schemas import ResponseSchema

router = BaseRouter(tags=['Избранное'])

@router.get(
    '/favourite',
    name="Возврат избранных товаров",
    response_model=List[FavouriteProductSchema],
    responses={
        status.HTTP_200_OK: {'model': List[FavouriteProductSchema]}
    },
)
async def get_products(session: AsyncSession = Depends(get_async_session)):
    """
    Возврат избранных товаров
    """

    products = await FavouriteService.get_list(session=session)

    return products


@router.post(
    '/favourite',
    name="Добавить товар в избранное",
    response_model=Union[FavouriteProductSchema, ResponseSchema],
    responses={
        status.HTTP_201_CREATED: {'model': FavouriteProductSchema},
        status.HTTP_404_NOT_FOUND : {'model': ResponseSchema}
    },
    status_code=status.HTTP_201_CREATED,
)
async def add_product(
    new_product: FavouriteAddSchema,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Добавить товар в избранное
    """
    record = await FavouriteService.add_product(
        new_product=new_product,
        session=session
    )

    return record

@router.delete(
    '/favourite/{product_id}',
    name="Удалить товар из избранного",
    response_model=ResponseSchema,
    responses={
        status.HTTP_200_OK: {'model': ResponseSchema},
        status.HTTP_404_NOT_FOUND : {'model': ResponseSchema}
    },
    status_code=status.HTTP_200_OK,
)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Удалить товар из избранного
    """
    await FavouriteService.delete_product(product_id=product_id, session=session)

    return ResponseSchema(detail='Товар удален из избранного')
