#!/usr/bin/env python3
""" module to train on async/await functions """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    diff = end - start
    return diff / 2
