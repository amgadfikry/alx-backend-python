#!/usr/bin/env python3
""" type-annotated function """
from typing import List

def sum_list(input_list: List[float]) -> float:
    """ sum_list - takes a list of floats as argument and returns their sum
    Args:
        input_list (list[float]): list of floats
    Returns:
        float: sum of floats
    """
    return sum(input_list)
