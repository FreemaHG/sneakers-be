from pydantic import BaseModel

from src.products.schemas.product import ProductSchema


class OrderSchema(BaseModel):
    """
    Схема для возврата данных о заказах с товарами
    """

    id: int
    products: list[ProductSchema]


class OrderCreateSchema(BaseModel):
    """
    Схема для создания нового заказа
    """

    products_id: list[int]
