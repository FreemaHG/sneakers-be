from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.products.models import Product


class Cart(Base):
    """
    Корзина с товарами
    """

    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='RESTRICT'))
    count: Mapped[int] = mapped_column(Integer, default=1)

    product: Mapped[Product] = relationship("Product", lazy='joined')
