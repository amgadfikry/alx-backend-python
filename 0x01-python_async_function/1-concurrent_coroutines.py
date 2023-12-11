#!/usr/bin/env python3
""" module to train on async/await functions """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    li = []
    for i in range(0, n):
        li.append(await wait_random(max_delay))
    sorted_li = await asyncio.to_thread(sorted, li)
    return sorted_li
