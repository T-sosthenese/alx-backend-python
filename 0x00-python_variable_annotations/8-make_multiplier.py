#!/usr/bin/env python3
"""
Module implementation for type-annotated callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an arg and returns a function
    that multiplies a float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Returns product of float and multiplier
        """
        return x * multiplier

    return multiplier_function
