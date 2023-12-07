#!/usr/bin/env python3
"""
A type-annotated function that takes input lists
and outputs their sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes list of floats as arg and outputs their float sum.
    """
    return sum(input_list)
