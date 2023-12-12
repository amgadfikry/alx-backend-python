#!/usr/bin/env python3
""" module to trainning on comprehension async """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure time """
    li = [async_comprehension() for i in range(4)]
    start = time.time()
    await asyncio.gather(*li)
    end = time.time()
    diff = end - start
    return diff
