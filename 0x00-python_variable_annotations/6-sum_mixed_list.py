#!/usr/bin/env python3
""" type-annotated function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list - takes a list of floats as argument and returns their sum
    Args:
        mxd_lst (list[Union[int, float]]): list of floats
    Returns:
        float: sum of floats
    """
    return sum(mxd_lst)
