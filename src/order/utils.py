from itertools import chain

from src.order.models import Order
from src.products.models.product import Product


async def get_unique_products(orders: list[Order]) -> list[Product]:
    """
    Возврат всех товаров переданных заказов
    :param orders: список заказов
    :return: список с товарами
    """
    products = set(chain.from_iterable([order.products for order in orders]))

    return products
