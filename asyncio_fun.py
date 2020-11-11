import asyncio
from asyncio.tasks import create_task
import time
from time import sleep
import typing


async def show_counter(number_of_items: int):
    for i in range(1, number_of_items):
        print(f"i is: {i}")
        await asyncio.sleep(0.25)


async def main():
    j = 1

    task = asyncio.create_task(show_counter(5))

    for j in range(1, 5):
        print(f"j is: {j}")
        await asyncio.sleep(1)

    await task

asyncio.run(main())
