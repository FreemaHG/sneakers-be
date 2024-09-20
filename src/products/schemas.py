from decimal import Decimal

from pydantic import BaseModel


class ProductSchema(BaseModel):
    """
    Схема для возврата данных о товаре
    """

    id: int
    title: str
    price: Decimal
    image: str
