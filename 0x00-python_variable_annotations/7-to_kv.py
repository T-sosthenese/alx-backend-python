#!/usr/bin/env python3
"""
Module implementation
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and OR float v and returns a tuple.
    The first element of tuple is string k, the second
    element is the square of v
    """
    return k, float(v ** 2)
