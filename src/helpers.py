"""Helper functions"""
from typing import Any, Callable


def can_convert(x: str, to_type: Callable[[str], Any]) -> bool:
    """Check if input can be converted to type

    :param x: input to be checked
    :type x: str
    :param to_type: converter function
    :type to_type: Callable[[str], Any]
    :returns: whether or not the input can be converted to desired type
    :rtype: bool
    """
    try:
        to_type(x)
        return True
    except Exception:
        return False
