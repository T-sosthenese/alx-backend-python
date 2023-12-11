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
    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
