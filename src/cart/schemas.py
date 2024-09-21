from decimal import Decimal

from pydantic import BaseModel, computed_field, Field

from src.products.schemas import ProductSchema


class CartSchema(BaseModel):
    """
    Схема для возврата данных о товаре в корзине
    """

    id: int
    product_id: int
    # count: int
    product: ProductSchema = Field(exclude=True)

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

    product_id: int
    count: int = Field(default=1)
