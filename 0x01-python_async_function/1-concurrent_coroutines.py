#!/usr/bin/env python3
"""
Module implementation for running multiple
coroutines at the same time.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    This function allows multiple coroutines to run concurrently.
    """
    list_of_delays = []
    for x in range(n):
        delays = await wait_random(max_delay)
        list_of_delays.append(delays)
    return sorted(list_of_delays)
