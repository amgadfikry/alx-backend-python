#!/usr/bin/env python3
""" type-annotated function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv - takes a string k and an int OR float v as arguments
    Args:
        k (str): string
        v (Union[int, float]): int OR float
    Returns:
        Tuple[str, float]: tuple of string and float
    """
    return (k, v * v)
