#!/usr/bin/env python3
""" type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function """
    def func(n: float) -> float:
        """ type-annotated function """
        return n * multiplier
    return func
