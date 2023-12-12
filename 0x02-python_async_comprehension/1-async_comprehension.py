#!/usr/bin/env python3
""" module to trainning on comprehension async """
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async function return list float """
    li = [i async for i in async_generator()]
    return li
