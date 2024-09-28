from decimal import Decimal

from pydantic import BaseModel, computed_field, Field

from src.products.schemas.product import ProductSchema


class CartSchema(BaseModel):
    """
    Схема для возврата данных о товаре в корзине
    """

    product: ProductSchema = Field(exclude=True)

    @computed_field()
    def id(self) -> int:
        return self.product.id

    @computed_field()
    def title(self) -> str:
        return self.product.title

    @computed_field()
    def price(self) -> Decimal:
        return self.product.price

    @computed_field()
    def image(self) -> str:
        return self.product.image


class CartAddSchema(BaseModel):
    """
    Схема для добавления товара в корзину
    """

    id: int
