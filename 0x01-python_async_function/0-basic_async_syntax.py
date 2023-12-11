#!/usr/bin/env python3
""" module to train on async/await functions """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ async function that await delay of provided random range
        Params:
            max_delay is range of delay with default 10
        Return:
            float of details
    """
    range: float = random.uniform(0, max_delay)
    await asyncio.sleep(range)
    return range
