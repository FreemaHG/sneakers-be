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

    def to_dict(self) -> dict:
        """
        Преобразование модели в словарь
        """
        model_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        model_dict['price'] = str(model_dict['price'])

        return model_dict
