#!/usr/bin/env python3
"""
A module that yields asynchronous values
"""

import asyncio
import random


async def async_generator():
    """
    An asynchronous function that generates asynchronous values
    without taking args
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
