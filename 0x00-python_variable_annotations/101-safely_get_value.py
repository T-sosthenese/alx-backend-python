#!/usr/bin/env bash
"""
Module implementation
"""


from typing import TypeVar, Mapping, Any, Union


# Define a generic type variable ~T
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Mapping dictionaries with keys of any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
