#!/usr/bin/env python3
""" type-annotated function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list - takes a list mxd_lst of floats and ints
    Args:
        mxd_lst (List[Union[int, float]]): list of floats and ints
    Returns:
        float: sum of floats and ints
    """
    return sum(mxd_lst)
