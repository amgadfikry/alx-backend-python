#!/usr/bin/env python3
""" module to train on async/await functions """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    range: float = random.uniform(0, max_delay)
    await asyncio.sleep(range)
    return range
