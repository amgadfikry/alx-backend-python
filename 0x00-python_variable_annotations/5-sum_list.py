#!/usr/bin/env python3
""" type-annotated function """


def sum_list(input_list: list[float]) -> float:
    """ sum_list - takes a list of floats as argument and returns their sum
    Args:
        input_list (list[float]): list of floats
    Returns:
        float: sum of floats
    """
    return sum(input_list)
