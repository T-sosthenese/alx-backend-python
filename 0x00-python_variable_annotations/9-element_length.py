#!/usr/bin/env python3
"""
Module implementation
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotates the parameters and returns values of the element_length func
    parameters:
    - lst: An iterable of sequences.

    Returns:
    - A list of tuples where each tuple contains a sequence of lst
    """
    return [(i, len(i)) for i in lst]
