from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Product(Base):
    """
    Товары
    """

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(150))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    image: Mapped[str] = mapped_column(String(150))
