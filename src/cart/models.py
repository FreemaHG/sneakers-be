from sqlalchemy import Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.products.models.product import Product


# вспомогательная таблица для связи корзин и товаров с отношением многие ко многим
# products_carts = Table(
#     'products_carts',
#     Base.metadata,
#     Column('cart_id', Integer, ForeignKey('cart.id'), primary_key=True),
#     Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
# )

# TODO Многие ко многим
# class Cart(Base):
#     """
#     Корзина с товарами
#     """
#
#     __tablename__ = 'cart'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
#     products: Mapped[list[Product]] = relationship('Product', secondary=products_carts, lazy='joined')


# TODO Один ко многим
class Cart(Base):
    """
    Корзина с товарами
    """

    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='RESTRICT'))

    product: Mapped[Product] = relationship("Product", lazy='joined')
