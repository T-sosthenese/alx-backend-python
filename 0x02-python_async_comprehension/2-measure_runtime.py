#!/usr/bin/env python3
"""
Module that measures the runtime for async generators
"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a coroutine that executes async_comprehension 4 times
    in parallel and measures their runtime
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime
