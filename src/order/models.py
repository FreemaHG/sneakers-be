from sqlalchemy import Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.products.models.product import Product


# вспомогательная таблица для связи заказов и товаров с отношением многие ко многим
products_orders = Table(
    'products_orders',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('order.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
)


class Order(Base):
    """
    Заказы с товарами
    """

    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    products: Mapped[list[Product]] = relationship('Product', secondary=products_orders, lazy='joined')
