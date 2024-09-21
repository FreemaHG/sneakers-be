from decimal import Decimal

from pydantic import BaseModel, Field, computed_field


class ProductSchema(BaseModel):
    """
    Схема для возврата данных о товаре
    """

    id: int
    title: str
    price: Decimal
    image: str
