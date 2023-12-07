#!/usr/bin/env python3
"""
A type-annotated function that takes a mixed list of ints
and floats and returns a float sum.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and floats and returns
    their sum as a float.
    """
    return sum(mxd_lst)
