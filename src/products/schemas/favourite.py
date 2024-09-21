from decimal import Decimal

from pydantic import BaseModel, Field, computed_field

from src.products.schemas.product import ProductSchema


class FavouriteProductSchema(BaseModel):
    """
    Схема для возврата данных об избранном товаре
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


class FavouriteAddSchema(BaseModel):
    """
    Схема для добавления товара в избранное
    """

    id: int
