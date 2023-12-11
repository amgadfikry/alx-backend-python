#!/usr/bin/env python3
""" module to train on async/await functions """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function return lit of awaited function result """
    li = [task_wait_random(max_delay) for _ in range(0, n)]
    waiting = await asyncio.gather(*li)
    return sorted(waiting)
