import asyncio
import json

from sqlalchemy import select

from src.database import async_session_maker
from src.products.models.product import Product


async def export_fixtures():

    async with async_session_maker() as session:
        query = select(Product)
        res = await session.execute(query)
        products = res.scalars().all()

        fixtures = [product.to_dict() for product in products]

        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(fixtures, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(export_fixtures())
