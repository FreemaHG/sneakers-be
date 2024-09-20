from typing import Optional, List

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_async_session
from src.products.schemas import ProductSchema
from src.products.services import ProductService
from src.router import BaseRouter
from src.schemas import ResponseSchema


router = BaseRouter(tags=['Товары'])

@router.get(
    '/products',
    name="Возврат товаров",
    description="Возврат товаров с возможностью фильтрации по названию и пагинацией",
    response_model=List[ProductSchema],
    responses={
        status.HTTP_200_OK: {'model': List[ProductSchema]}
    },
)
async def get_products(
    title: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Возврат товаров
    """

    products = await ProductService.get_list(title=title, limit=limit, offset=offset, session=session)

    return products


@router.get(
    '/products/{product_id}',
    name="Возврат товара",
    description="Возврат товара по идентификатору",
    response_model=ProductSchema,
    responses={
        200: {'model': ProductSchema},
        404: {'model': ResponseSchema},
    }
)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возврат товара
    """

    post = await ProductService.get(product_id=product_id, session=session)

    if not post:
        raise HTTPException(status_code=status.NOT_FOUND, detail='Товар не найден')

    return post
