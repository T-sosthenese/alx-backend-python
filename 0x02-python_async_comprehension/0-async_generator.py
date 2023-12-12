#!/usr/bin/env python3
"""
A module that yields asynchronous values
"""

import asyncio
import random
from typing import Generator


async def async_generator() ->Generator[float, None, None]:
    """
    An asynchronous function that generates asynchronous values
    without taking args
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
