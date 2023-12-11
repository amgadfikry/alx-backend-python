#!/usr/bin/env python3
""" module to train on async/await functions """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ function return lit of awaited function result """
    li = [wait_random(max_delay) for _ in range(0, n)]
    waiting = await asyncio.gather(*li)
    return waiting
