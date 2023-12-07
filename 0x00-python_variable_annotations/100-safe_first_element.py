#!/usr/bin/env python3
""" type-annotated function """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe_first_element - takes a lst of any type and returns first element
    Args:
        lst (Sequence[Any]): list of any type
    Returns:
        Union[Any, None]: first element of lst or None if lst is empty
    """
    if lst:
        return lst[0]
    else:
        return None
