#!/usr/bin/env python3
""" module to trainning on comprehension async """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """ generate a generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
