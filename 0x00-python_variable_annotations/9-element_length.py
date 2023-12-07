#!/usr/bin/env python3
""" type-annotated function """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length - takes a list lst of strings and returns
        a list of tuples, each tuple having the string
        and its length
    Args:
        lst (Iterable[Sequence]): list of strings
    Returns:
        List[Tuple[Sequence, int]]: list of tuples, each tuple having the
                                    string and its length
    """
    return [(i, len(i)) for i in lst]
