import asyncio
import json

from src.database import async_session_maker
from src.products.models.product import Product


async def import_fixtures():

    async with async_session_maker() as session:
        with open('products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            product = Product(id=item['id'], title=item['title'], price=item['price'], image=item['image'])
            session.add(product)

        await session.commit()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(import_fixtures())
