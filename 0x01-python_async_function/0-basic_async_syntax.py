#!/usr/bin/env python3
"""
Module implementation for async function
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous function that returns a random float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
