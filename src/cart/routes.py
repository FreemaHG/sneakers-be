from typing import List, Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.cart.schemas import CartSchema, CartAddSchema
from src.cart.services import CartService
from src.database import get_async_session
from src.router import BaseRouter
from src.schemas import ResponseSchema


router = BaseRouter(tags=['Корзина'])

@router.get(
    '/cart',
    name="Возврат товаров в корзине",
    response_model=List[CartSchema],
    responses={
        status.HTTP_200_OK: {'model': List[CartSchema]}
    },
    status_code=status.HTTP_200_OK
)
async def get_products(session: AsyncSession = Depends(get_async_session)):
    """
    Возврат товаров в корзине
    """
    records = await CartService.get_list(session=session)

    return records


@router.post(
    '/cart',
    name="Добавить товар в корзину",
    response_model=Union[CartSchema, ResponseSchema],
    responses={
        status.HTTP_201_CREATED: {'model': CartSchema},
        status.HTTP_404_NOT_FOUND : {'model': ResponseSchema}
    },
    status_code=status.HTTP_201_CREATED,
)
async def add_product(
    new_product: CartAddSchema,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Добавить товар в корзину
    """
    record = await CartService.add_product(
        new_product=new_product,
        session=session
    )

    return record

@router.delete(
    '/cart/{product_id}',
    name="Удалить товар из корзины",
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
    Удалить товар из корзины
    """
    await CartService.delete_product(product_id=product_id, session=session)

    return ResponseSchema(detail='Товар удален из корзины')
