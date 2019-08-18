"""CLI helper to collect user input"""
import sys
from typing import Any, Callable


def prompt(text: str,
           strip: bool = True,
           required: bool = True,
           check: Callable[[str], bool] = lambda x: True,
           transform: Callable[[Any], Any] = lambda x: x
           ) -> Any:
    """Prompts user for input

    :param text: Label for user-input
    :type text: str
    :param strip: Whether to strip user input (default is True)
    :type strip: bool
    :param required: Whether user-input is required (default is True)
    :type required: bool
    :param check: Function that takes input and returns a boolean indicating
        whether input passed check (default is lambda x: True)
    :type check: Callable[[str], bool]
    :param transform: Transformer function to be applied before returning
        (default is lambda x: x)
    :type transform: Callable[[Any], Any]
    :returns: result of prompt
    :rtype: Any
    """
    while True:
        try:
            selection = input(text + " ")
            if strip:
                selection = selection.strip()
        except (EOFError, KeyboardInterrupt):
            sys.exit(1)
        if required and not selection:
            continue
        if check and selection and not check(selection):
            print("Invalid input")
            continue
        break
    return transform(selection)


def collect(collection: dict) -> dict:
    """Collect user input in dictionary

    :param collection: input dictionary with questions to collect. Every value
    must be a dictionary with a "text" key and optionally "strip", "required",
    "check" and "transform" keys (see: prompt)
    :type collection: dict
    :returns: collection with same keys as input and corresponding user-inputs
    :rtype: dict
    """
    result = dict()

    for key, value in collection.items():
        result[key] = prompt(**value)

    return result
