from typing import Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_async_session
from src.order.schemas import OrderSchema, OrderCreateSchema
from src.order.services import OrderService
from src.router import BaseRouter
from src.schemas import ResponseSchema


router = BaseRouter(tags=['Заказы'])

@router.get(
    '/orders',
    name="Возврат заказов",
    response_model=list[OrderSchema],
    responses={
        status.HTTP_200_OK: {'model': list[OrderSchema]}
    },
    status_code=status.HTTP_200_OK
)
async def get_orders(session: AsyncSession = Depends(get_async_session)):
    """
    Возврат заказов
    """
    orders = await OrderService.get_list(session=session)

    return orders


@router.post(
    '/orders',
    name="Создать заказ",
    response_model=Union[OrderSchema, ResponseSchema],
    responses={
        status.HTTP_201_CREATED: {'model': OrderSchema},
        status.HTTP_404_NOT_FOUND : {'model': ResponseSchema}
    },
    status_code=status.HTTP_201_CREATED,
)
async def create(
    data: OrderCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создать заказ
    """
    record = await OrderService.create(products_ids=data.products_id, session=session)

    return record
