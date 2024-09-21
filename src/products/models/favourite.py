from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.products.models.product import Product


class FavouriteProduct(Base):
    """
    Избранные товары
    """

    __tablename__ = 'favourite_product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='RESTRICT'))

    product: Mapped[Product] = relationship("Product", lazy='joined')
